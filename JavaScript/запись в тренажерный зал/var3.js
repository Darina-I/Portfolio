function prov(){
	if ((event.keyCode < 48) || (event.keyCode > 57)){
		event.returnValue = false;
	alert('Данные введены неверно');
}}
function count(){
	var sp;
	var cost=0;
	if(document.info.sport[0].checked==true){
		sp = 'Беговая дорожка';
		cost = document.info.sport[0].value;}
	else if(document.info.sport[1].checked==true){
		sp = 'Штанга';
		cost = document.info.sport[1].value;}
	else if(document.info.sport[2].checked==true){
		sp = 'Жим от груди';
		cost = document.info.sport[2].value;}
	else if(document.info.sport[3].checked==true){
		sp = 'Баттерфляй';
		cost = document.info.sport[3].value;}
	var hour=Number(document.getElementById('text').value);
	cost*=hour;
	var day;
	if(document.info.day[0].checked==true){
		day = document.info.day[0].value;
		cost *= 0.95;}
	else if(document.info.day[1].checked==true){
		day=document.info.day[1].value;}
	else if(document.info.day[2].checked==true){
		day=document.info.day[2].value;}
	else if(document.info.day[3].checked==true){
		day=document.info.day[3].value;
		cost*=0.9;}
	document.getElementById('result').value=sp+' '+'\n'+'Количество часов: '+hour+'\n'+day+'\n'+'Всего: '+cost+' p.';
	
}
	

	