function prov1(){//проверяет, что в поле кол-во часов вводятся только цифры
	if ((event.keyCode < 48) || (event.keyCode > 57)){
	event.returnValue = false;
	alert('Данные введены неверно');
}}
function prov2(){//делаем кнопку доступной или нет
	var kol = document.getElementById("kol");
	if(kol!=''){document.getElementsByClassName("but")[0].disabled=false;}
	else{document.getElementsByClassName("but")[0].disabled=true;}
}
function can(){//выводим в стоимость цены в зависимость от выбранного статуса
	var cost =0;
	var list=[];
	var el = document.getElementById('st');
	cost=el.value;
	var textt=el.text;
	document.getElementById('cena').value=cost;
}
function vcee(){
	var vce=[];
	var l = Array.from(langs.options).filter(option => option.selected).map(option => option.value);/*filter-проверяет каждый элемент, 
	а не первый попавшийся, который возвращает true; map-вызывает функцию для каждого элемента массива 
	и возвращает массив результатов выполнения этой функции.*/
	var len=l.length;
	var cen=Number(document.getElementById('st').value);
	var k=Number(document.getElementById("kol").value);
	var cos = k*cen*len;
	vce.push('Для изучения выбран:'+'\n'+l+' по '+cen+'руб. за час'+'\n'+'Стоимость: '+cos);
	document.getElementById('result').value=vce.join(' ');
}

	
	
