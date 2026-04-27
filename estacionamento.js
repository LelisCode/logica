//entrada
let HE = parseInt(window.prompt("Em que horario o senhor(a) entrou? (0-23):"));
let ME = parseInt(window.prompt("Em que minuto senhor(a) entrou? (0-59):"));
let HS = parseInt(window.prompt("Em que horario o senhor(a) saiu? (0-23):"));
let MS = parseInt(window.prompt("Em que minuto o senhor(a) saiu? (0-59):"));

//Validação

if (HE > 23 ||HE < 0 || HE > 59 || HE < 0 || HS > 23 || HS <0 || MS > 59 || MS < 0 || Number.isNaN(HE) || Number.isNaN(HS) || Number.isNaN(ME) || Number.isNaN(MS))

 {  document.write("Valores inválidos!");
}


//Convertendo as horas para minutos
else {
let TS = 60 * HS + MS;
let TE = 60 * HE + ME;

//Calculo do horário em que a pessoa permaneceu
let TT = TS - TE;

// caso vire o dia
if (TT < 0) {
  TT = TT + 24 * 60;
}

// Calculo caso tenha minutos extras 
if (TT % 60 != 0) {
  TT = TT + (60 - (TT % 60));
}


// transforma em horas inteiras
TT = TT / 60;

//Valor 
let V = 0;

if (TT <= 1){ 
    V = 4;
}

else if (TT <= 2) {
    V = 6;
}

else  {

    V = 6 + (TT - 2) * 1;
}

//Saída

document.write("O valor a ser pago será R$:" + V);
}



