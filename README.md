# SnmpProject

### Front

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 13.3.2.

### Back

This

## Development server [frontend]

Run `ng serve --o` for a dev server. Wait and page is open to `http://localhost:4200/`. The application will automatically reload if you change any of the source files.

## Development server [backend]

### First Step:

configure your snmp. If you don't know, read the website:
`https://www.makeuseof.com/install-and-configure-snmp-on-windows-10/#:~:text=SNMP%20is%20available%20as%20an,Provider%20and%20click%20on%20Install.Ao`

### Second Step:

Open your `CMD` and install Flask, CORS and Waitress with:
`pip install Flask` >> Flask
`pip install -U flask-cors` >> CORS
`pip install waitress` >> Waitress

### Third Step:

Open with python in your cmd the document `serverFlask.py`. Navigate to `http://localhost:8889/`. The application print "Api it's works".
