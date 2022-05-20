from struct import pack
import socket


def mensagem_SNMP(OID,ipDest=b'127.0.0.1'):

    ### Definindo parâmetros do SNMP
	
    COMM=b'public'    

    ### Definindo parâmetros do gerente

    portDest = 161

    ## Criando conexão no socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # verifica criação do socket
    if(s == -1):
        print('\n\nNão foi possível criar o socket')
    else:
        print('\n\nsocket foi criado em ', s, ('\n'))

    ### Montando mensagem SNMP de trás pra frente

    # Value field
    val = b'mensagem de teste do snmp'
    snmpVal = pack("bb{}s".format(len(val)),4,len(val),val) #byte 0x05  - data type nulo

    # Object Field
    OID = OID.split(".")  #System Description
    snmpOid = pack("2b",0x2b, 0x06) + bytearray(int(x) for x in OID ) # adicionando iso.3 ao OID

    # Sequence / Varbind Type Field
    snmpVarbind = snmpOid + snmpVal
    snmpVarbindSeq = pack('b',6) + len(snmpOid).to_bytes(1,'little') + snmpVarbind 

    # Sequence / Varbind List Field
    snmpVarbindList = pack('b',0x30) + len(snmpVarbindSeq).to_bytes(1,"little") + snmpVarbindSeq
    snmpVarbindList = pack('b',0x30) + len(snmpVarbindList).to_bytes(1,"little") +  snmpVarbindList

    # Error Index
    ErrIndex = pack("b",0x0)
    pdu = pack("b",0x02) + len(ErrIndex).to_bytes(1,"little") +  ErrIndex + snmpVarbindList

    # Error
    Err = pack("b",0x0)
    pdu = pack('b',2) + len(Err).to_bytes(1,"little") + Err + pdu

    # Request ID
    RqID = pack("b",0x2)
    pdu = pack('b',2) + len(RqID).to_bytes(1,"little") + RqID + pdu

    pduType =  pack('B',0xa0) # 0xa0 = getRequest, 0xa2 = getResponse
    pdu = pduType + len(pdu).to_bytes(1,"little") + pdu

    # Community
    lenComm = len(COMM)
    snmpComm = pack("{}s".format(lenComm),COMM)

    snmpProtocolHeader = pack('b',0x04) + lenComm.to_bytes(1,"little") + snmpComm + pdu


    # Versão
    snmpVersion = pack('b',0x0)
    snmpProtocolHeader = pack('b',0x2) + len(snmpVersion).to_bytes(1,"little") + snmpVersion + snmpProtocolHeader


    # Mensagem SNMP Final
    snmpMessage = pack('b',0x30) + len(snmpProtocolHeader).to_bytes(1,"little") + snmpProtocolHeader

    #print(f'Mensagem SNMP raw bytes:\n{snmpMessage}')

    ## Transmitindo mensagem

    s.sendto(snmpMessage,(ipDest,portDest))

    try:
        Rxbuf = s.recv(2000)#tamanho dos dados pro buffer
        # print(f'Resposta Recebida >>> {Rxbuf.decode("utf-8", errors="ignore")}')
        response = Rxbuf.decode("utf-8", errors="ignore")
        return(response)
    
    except socket.timeout:
        #print ('time out!!!')
        s.close()
        print ('\n\nFim da Operacao. Socket fechado. \n Time out!!!')
        return "time out!!!"

print(mensagem_SNMP('1.2.1.1.1.0') + '\n-----------------------------------------------------------------------------------------------')



#Rest com python usando Flask:

import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# funcionalidades 

@app.route("/")
def start_api():
    return "Api it's works"

@app.route("/response", methods=['POST'])
def response_snmp():
    r = request.get_json()
    dataAux = r['oid']
    dataAux2 = r['ip']
    return jsonify(mensagem_SNMP(dataAux, dataAux2))

#rodando a api

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8889)