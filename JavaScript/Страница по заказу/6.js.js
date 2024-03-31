function new_window(){
	if(typeof new_w !== 'undefined'){new_w.window.close();}
	var ttext='<p>'+document.getElementById('text').value+'</p>';	
	new_w=window.open("","","width=450,height=500");
	var css1;
	var css2;
	var css3;
	console.log(draw);
	new_w.document.write(ttext);	
	if(document.getElementById('italic').checked){css1="font-style:italic;";}
	else{css1='';}
	if(document.getElementById('under').checked){css2="text-decoration:underline;";}
	else{css2='';}	
	if(document.getElementById('bold').checked){css3="font-weight:bold;";}
	else{css3='';}
	var i = document.getElementById('draw').options[document.getElementById('draw').selectedIndex].value;
	var img='<img src=\"'+i+'\">';
	new_w.document.write(img);
	for(let i=0;i<3;i++){
		if(document.getElementsByName('fon')[i].checked){var f = document.getElementsByName('fon')[i].value;}}
	var fon="background-image:url("+f+");";
	console.log(fon);	
	new_w.document.body.style.cssText=css1+css2+css3+"background-image:url("+f+");";
	new_w.document.write("<br><input type=\"button\" value=\"Закрыть\" onclick=\"window.close()\">");
}