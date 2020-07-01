jQuery(document).ready(function($) {
    $('.button').hover(function() {
  $( this ).fadeOut( 100 );
  $( this ).fadeIn( 500 );
});
});











function myFunction() {
var method7 = document.getElementsByName('RadioButtonList7');
var method6 = document.getElementsByName('RadioButtonList6');
var method5 = document.getElementsByName('RadioButtonList5');
var method1 = document.getElementsByName('RadioButtonList4');
var method2 = document.getElementsByName('RadioButtonList3');
var method3 = document.getElementsByName('RadioButtonList2');
var method4 = document.getElementsByName('RadioButtonList1');



var loop = true;
var ischecked_method = false;
document.getElementById('bigpic').hidden="";


while(loop == true){




ischecked_method = false;
for ( var j = 0; j < method1.length; j++) {
        if(method1[j].checked) {
            ischecked_method = true;

         
    }

}

if(!ischecked_method)   { 
    alert("Please choose item ");
    document.getElementById('bigpic').hidden="hidden";
}

break;





ischecked_method = false;
for ( var j = 0; j < method4.length; j++) {
        if(method4[j].checked) {
            ischecked_method = true;

         
    }

}

if(!ischecked_method)   { 
    alert("Please choose item ");
    document.getElementById('bigpic').hidden="hidden";
}

break;



ischecked_method = false;
for ( var a = 0; a < method2.length; a++) {
        if(method2[a].checked) {
            ischecked_method = true;

         
    }

}

if(!ischecked_method)   { 
    alert("Please choose item ");
    document.getElementById('bigpic').hidden="hidden";
}
break;


ischecked_method = false;
for ( var a = 0; a < method6.length; a++) {
        if(method6[a].checked) {
            ischecked_method = true;

         
    }

}

if(!ischecked_method)   { 
    alert("Please choose item ");
    document.getElementById('bigpic').hidden="hidden";
}
break;



ischecked_method = false;
for ( var a = 0; a < method7.length; a++) {
        if(method7[a].checked) {
            ischecked_method = true;

         
    }

}

if(!ischecked_method)   { 
    alert("Please choose item ");
    document.getElementById('bigpic').hidden="hidden";
}
break;




ischecked_method = false;
for ( var a = 0; a < method3.length; a++) {
        if(method3[a].checked) {
            ischecked_method = true;

         
    }

}

if(!ischecked_method)   { 
    alert("Please choose item ");
    document.getElementById('bigpic').hidden="hidden";
}
break;


ischecked_method = false;
for ( var j = 0; j < method5.length; j++) {
        if(method5[j].checked) {
            ischecked_method = true;

         
    }

}

if(!ischecked_method)   { 
    alert("Please choose item ");
    document.getElementById('bigpic').hidden="hidden";
}
break;



}


loop =true ;





var pic = "bigpic"
        



        var v=0;
        var r=0;
        var t=0;
        var y;


if(RadioButtonList1_0.checked)
    v++;
else if(RadioButtonList1_1.checked)
    v=v+3;
else if(RadioButtonList1_2.checked)
    v=v+7;
else if(RadioButtonList1_3.checked)
    v=v+10;






if(RadioButtonList2_0.checked)
    v=v+0;
else if(RadioButtonList2_1.checked)
    v=v+1;
else if(RadioButtonList2_2.checked)
    v=v+4;
else if(RadioButtonList2_3.checked)
    v=v+8;







if(RadioButtonList3_0.checked)
    r++;
else if(RadioButtonList3_1.checked)
    r=r+3;
else if(RadioButtonList3_2.checked)
    r=r+5;
else if(RadioButtonList3_3.checked)
    r=r+7;






if(RadioButtonList4_0.checked)
    r=r+0;
else if(RadioButtonList4_1.checked)
    r=r+4;
else if(RadioButtonList4_2.checked)
    r=r+8;





if(RadioButtonList5_0.checked)
    r=r+2;
else if(RadioButtonList5_1.checked)
    r=r+5;
else if(RadioButtonList5_2.checked)
    r=r+7;









if(RadioButtonList6_0.checked)
    r+0;
else if(RadioButtonList6_1.checked)
    r=r+2;
else if(RadioButtonList6_2.checked)
    r=r+5;
else if(RadioButtonList6_3.checked)
    r=r+8;




if(RadioButtonList7_0.checked)
    r=r+0;
else if(RadioButtonList7_1.checked)
    r=r+3;
else if(RadioButtonList7_2.checked)
    r=r+6;
else if(RadioButtonList7_3.checked)
    r=r+8;
else 
    r=r+10;

t=0.6*v + 0.4*r;


if(t < 8)
    y = document.getElementById('bigpic').src="Img/1.jpeg";

else if (t > 7 && t < 12)
    y = document.getElementById('bigpic').src="Img/2.jpeg";

else if (t > 11 && t < 14 )
    y = document.getElementById('bigpic').src="Img/3.jpeg";

else if (t > 13 && t < 17 )
    y = document.getElementById('bigpic').src="Img/4.jpeg";

else if (t > 16 && t < 21)
    y = document.getElementById('bigpic').src="Img/5.jpeg";

else if (t > 20 && t < 24)
    y = document.getElementById('bigpic').src="Img/6.jpeg";

else if (t > 23 && t < 27)
    y = document.getElementById('bigpic').src="Img/7.jpeg";

else if (t > 26)
    y = document.getElementById('bigpic').src="Img/8.jpeg";



/*




switch (v) {

    case 1:
        y = document.getElementById('bigpic').src="Img/v=0.png";
        
        break;
    case 2:
        y = document.getElementById('bigpic').src="Img/v=1.png";
        break;
    case 3:
        y = document.getElementById('bigpic').src="Img/v=2.png";
        break;
    case 4:
        y = document.getElementById('bigpic').src="Img/v=3.png";
        break;
    case 5:
        y = document.getElementById('bigpic').src="Img/v=4.png";
        break;
}

*/


}