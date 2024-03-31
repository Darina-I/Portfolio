function prov(){
	var name=document.getElementById('name').value;
	var kol=Number(document.getElementById('kol').value);
	var cost=Number(document.getElementById('cost').value);
	var all1=Number(document.getElementById('all1').value);
	if (name!='' && kol!='' && cost!='' && all1!=''){
		document.getElementById('but').disabled = false;}
	else{document.getElementById('but').disabled = true;}
}
function result(){
	var name=document.getElementById('name').value;
	var kol=Number(document.getElementById('kol').value);
	var cost=Number(document.getElementById('cost').value);
	var all1=Number(document.getElementById('all1').value);
	var ost=kol-all1;
	var summa1=all1*cost;
	var summa2=ost*cost;
	if(!(isNaN(ost) && isNaN(summa1) && isNaN(summa2))){
		document.getElementById('ost').value= ost;
		document.getElementById('summa1').value = summa1;	 
		document.getElementById('summa2').value = summa2;}
	else{alert('Данные введены неверно!')}
}
function close1(){window.close();}
function res(){document.getElementById('but').disabled = true;}