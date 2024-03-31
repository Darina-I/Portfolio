function reg(){	
	var fio_reg=/[А-Я][а-я]{1,} [А-Я][а-я]{1,}/;
	var adr_reg=/ул\.[А-Я][а-я]{1,} д\.[1-9][0-9]{0,} кв\.[1-9][0-9]{0,}/;
	var tel_reg=/(\+7[ ]?[0-9]{2}\-[0-9]{2}\-[0-9]{2}\-[0-9]{2}\-[0-9]{2})|(8[ ]?[0-9]{3}\-[0-9]{3}\-[0-9]{4})/;
	var snils_reg=/[0-9]{3}\-[0-9]{3}\-[0-9]{3}[ ][0-9]{2}/;
	var fio=document.getElementById("fio").value;
	var adr=document.getElementById("adr").value;
	var tel=document.getElementById("tel").value;
	var email=document.getElementById("email").value;
	var snils=document.getElementById("snils").value;
	var dis=0;
	if(fio_reg.test(fio)==true && (fio.length>3 && fio.length<40)){console.log("fio: DA");}
	if(adr_reg.test(adr)==true){console.log("dom: DA");}
	if(tel_reg.test(tel)==true){console.log("tel: DA");}
	if(snils_reg.test(snils)==true){
		var sum=0;
		var mas1=snils.split(' ');
		var kontr=mas1[1];
		var nomer1=mas1[0].split('-');
		var nomer2=[];
		for(let i=0;i<nomer1.length;i++){
			let k=nomer1[i].split('');
			for(let j=0;j<k.length;j++){nomer2.push(k[j]);}}
		nomer2=nomer2.reverse();
		for(let i=0;i<nomer2.length;i++){sum+= (i+1)*nomer2[i];}
		if(sum==100 && sum==101){sum==00}
		else if(sum>101){sum=Math.floor(sum/101);}
	if(fio_reg.test(fio) && (fio.length>3 && fio.length<40) && adr_reg.test(adr) && tel_reg.test(tel) && document.getElementById('email').value!='' && snils_reg.test(snils) && sum==kontr){document.getElementById('but').disabled=false;}
	else{document.getElementById('but').disabled=true; alert('Данные введены неверно');}
}}