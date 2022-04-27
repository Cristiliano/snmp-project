import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { SnmpService } from 'src/app/services/snmp.service';

@Component({
  selector: 'app-input-container',
  templateUrl: './input-container.component.html',
  styleUrls: ['./input-container.component.scss'],
})
export class InputContainerComponent implements OnInit {
  oneForm!: FormGroup;
  resposta: string = '';

  constructor(private fb: FormBuilder, private snmp: SnmpService) {}

  ngOnInit(): void {
    this.setElem();
  }

  ngAfterViewInit() {}

  setElem() {
    this.oneForm = this.fb.group({
      name: '',
      value: '',
    });
  }

  onSubmit() {
    const obj = {
      oid: `${this.oneForm.get('name')?.value}`,
      ip: `${this.oneForm.get('value')?.value}`,
    };

    this.snmp.snmpResponse(obj).subscribe((e) => {
      this.resposta = e;
    });
  }
}
