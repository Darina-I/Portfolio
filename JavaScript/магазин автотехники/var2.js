var cena=[451000, 1200, 4500, 12000, 16000];
var vivod=[];
function count1(){
	let kol=0;
	let cost=0;
	if(document.info.nam1.checked==true){
		cost += Number(cena[0]);
		kol+=1;
		document.getElementById("photo").src="baz.jpg";}
	if(document.info.nam2.checked==true){
		cost +=Number(cena[1]);
		kol+=1;
		document.getElementById("photo").src="kov.jpg";}
	if(document.info.nam3.checked==true){
		cost+=Number(cena[2]);
		kol+=1;
		document.getElementById("photo").src="kar.jpg";}
	if(document.info.nam4.checked==true){
		cost+=Number(cena[3]);
		kol+=1;
		document.getElementById("photo").src="shin.jpg";}
	if(document.info.nam5.checked==true){
		cost+=Number(cena[4]);
		kol+=1;
		document.getElementById("photo").src="disk.png";}
	if(kol==5){cost*=0.9;}
	document.getElementById('result').value=cost;
	cost=0;
}
function but(){
	var cost2=0;
	var kol=0;
	var elem=['Базовая комплектация', 'Коврики', 'Защита картера', 'Зимние шины', 'Литые диски'];
	for(let i=0;i<6;i++){
		if(document.getElementsByTagName('input')[i].checked==true){
			cost2+=Number(document.getElementsByTagName('input')[i].value);
			vivod.push(elem[i]);
			vivod.push(cena[i]);
			vivod.push('\n');
			kol+=1
		}
	}
	if(kol==5){vivod.push('Скидка: 10%'+'\n');}
	vivod.push('Всего: '+cost2);
	alert(vivod.join(' '));
    vivod=[];
}



