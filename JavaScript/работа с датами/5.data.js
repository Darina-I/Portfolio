function prov(){
	var reg=/(^(0[0-9]|[1-9]|[12][0-9]|3[01])[.-\/](0[13578]|[13578]|1[02])[.-\/]([0-9]{2}|19[0-9]{2}|20[0-9]{2})$)|(^(0[1-9]|[1-9]|[12][0-9]|30)[.-\/](0[469]|[469]|11)[.-\/]([0-9]{2}|19[0-9]{2}|20[0-9]{2})$)|(^(0[1-9]|[1-9]|[12][0-9])[.-\/](02|2)[.-\/]([0-9]{2}|19[0-9]{2}|20[0-9]{2})$)/;  
	var one_date=document.getElementById('one').value;	
	var two_date=document.getElementById('two').value;
	console.log(one_date);
	console.log(two_date);
	var c;
	if(reg.test(one_date)==true){
	one_date=one_date.split(/\.|\/|\-/);
	one_date=one_date.reverse();
	one_date=one_date.join('.');		
	one_date=Date.parse(one_date);
	two_date=Date.parse(two_date);
	console.log(one_date);
	console.log(two_date);
	if(two_date>one_date){
		for(let i=0; i<5; i++){if(document.getElementsByName('day')[i].checked){c = i+1; console.log(c);}}
		switch(c){
			case 1://КОЛИЧЕСТВО ДНЕЙ
				var S = two_date-one_date;
				console.log(S)
				var kol = Math.floor(S/86400000);					
				console.log('kol'+kol);	
				document.getElementById('res').value=kol +' дн.';break;
			case 2://КОЛИЧЕСТВО ВЫХОДНЫХ
				var S = two_date-one_date;
				var kol = Math.floor(S/86400000);
				var WEE=0;
				one_date2=new Date(one_date);
				two_date2=new Date(two_date);
				var D1 = one_date2.getDay();
				console.log('D'+D1);
				for(let i=0;i<=kol;i++){
					if(D1==6 || D1==0){WEE+=1; console.log('+');}												
					one_date=one_date+86400000;
					one_date2=new Date(one_date);
					D1 = one_date2.getDay();}
				console.log('WEE'+WEE);
				document.getElementById('res').value=WEE+' дн.';break;			
			case 3://КОЛИЧЕСТВО РАБОЧИХ ДНЕЙ
				var S = two_date-one_date;
				var kol = Math.floor(S/86400000)+1;
				var WEE=0;
				one_date2=new Date(one_date);
				two_date2=new Date(two_date);
				var D1 = one_date2.getDay();
				for(let i=0;i<=kol;i++){
					if(D1==6 || D1==0){WEE+=1;}												
					one_date=one_date+86400000;
					one_date2=new Date(one_date);
					D1 = one_date2.getDay();}
				var WOOK=kol-WEE;
				console.log('WOOK'+WOOK);
				document.getElementById('res').value=WOOK+' дн.';break;
			case 4://КОЛИЧЕСТВО ПОЛНЫХ НЕДЕЛЬ
				one_date2=new Date(one_date);
				var D = one_date2.getDay();
				if(D!=1){
					while(D!=1){
						one_date=one_date+86400000;
						one_date2=new Date(one_date);
						var D = one_date2.getDay();}}
				if(D==1){
					S=two_date-one_date;
					var FULL= Math.floor(S/604800000);}
				console.log('FULL'+FULL);
				document.getElementById('res').value=FULL+' нед.';break;
			case 5://КОЛИЧЕСТВО ПОЛНЫХ МЕСЯЦЕВ
				one_date2=new Date(one_date);
				two_date2=new Date(two_date);
				var M=one_date2.getMonth();
				var D=one_date2.getDate();
				if((M==0 || M==2 || M==4 || M==6 || M==7 || M==9 || M==11)&& one_date<two_date){
					if(D!=1){
					while(D!=1){
						one_date=one_date+86400000;
						one_date2=new Date(one_date);
						var D = one_date2.getDate();}}
					if(D==1 && one_date<two_date){
						S=two_date-one_date;
						var FULL_M= Math.floor(S/2678400000);}//31						
						D = one_date2.getDate();}
				else if(M==1 && one_date<two_date){
					if(D!=1){
					while(D!=1){
						one_date=one_date+86400000;
						one_date2=new Date(one_date);
						var D = one_date2.getDate();}}
					if(D==1 && one_date<two_date){
						S=two_date-one_date;
						var FULL_M= Math.floor(S/2505600000);}	//28						
						D = one_date2.getDate();}
				else if( (one_date<two_date)&&(M==3 || M==5 || M==8 || M==10)){
					if(D!=1){
					while(D!=1){
						one_date=one_date+86400000;
						one_date2=new Date(one_date);
						var D = one_date2.getDate();}}
					if(D==1 && one_date<two_date){
						S=two_date-one_date;
						var FULL_M= Math.floor(S/2592000000);}//30							
						D = one_date2.getDate();}
				console.log('FULL_M'+FULL_M);
				document.getElementById('res').value=FULL_M+' мес.';break;
			}
		}
		else{alert("Данные введены неверно!");}
	}
	else{alert("Данные введены неверно!");}
}	
