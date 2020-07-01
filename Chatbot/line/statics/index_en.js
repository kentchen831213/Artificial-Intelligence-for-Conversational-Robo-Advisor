window.onload = function speak(){
	var synth = window.speechSynthesis;
    var utterThis = new SpeechSynthesisUtterance('Welcome!');
	utterThis.pitch = 1;
    utterThis.rate = 1;
    utterThis.lang = 'en';
	synth.speak(utterThis);
};



$(".button-collapse").sideNav();
resize()
window.onresize = resize;
function resize(){
 $('.card.brown.lighten-2').height($( window ).height()-160);
 if ($( window ).width() >=993){
	$('#chatbox').height($( window ).height()-255);
	$('#chatbox_content').height($( window ).height()-255);
	$('.panel-body').height($( window ).height()-275);
 }else {
	$('#chatbox').height($( window ).height()-214);
	$('#chatbox_content').height($( window ).height()-214);
	$('.panel-body').height($( window ).height()-234);
 }
}
var query = ''
var date1 = new Date();
var date2 = new Date();

$( document ).ready(function() {
	if (document.images) {
		var img1 = new Image();
		img1.src = "/img/user.png";
	}

	var synth = window.speechSynthesis;
	var state = 0;

	function speak(inputTxt){
	  if(inputTxt !== ''){
		var utterThis = new SpeechSynthesisUtterance(inputTxt);
		utterThis.pitch = 1;
		utterThis.rate = 1;
		synth.speak(utterThis);
	  }
	}

	var request = function(e) {
		state = 0;
		query = $('#input_text').val();
		$('#input_text').val('');
        $(".chat").append('<li class="clearfix"><div class="message row"></div><div class="col s10 m10 l10 chat-body clearfix right"><img src="/img/user.png" alt="User Avatar" class="mfr circle responsive-img" align="right"><p class="right">' + query + '</p></div></li>');
		$(".panel-body").stop().animate({
			scrollTop: $(".panel-body")[0].scrollHeight
		}, 1000);
		function response(){
			if (state == 0){
			
				$(".panel-body").stop().animate({
					scrollTop: $(".panel-body")[0].scrollHeight
				}, 1000);}
		}
		setTimeout(response, 1000);
	};

	var submit_form = function(e) {
		$.getJSON($SCRIPT_ROOT + '/_add_numbers', {
			query: query,
		}, function(data) {
			speak(data.result)
            $(".chat").append('<li class="clearfix"><div class="message row"></div><div class="col s10 m10 l10 chat-body clearfix left"><img src="/img/AIWISFIN.png" alt="User Avatar" class="mfr circle responsive-img" align="left"><p class="left">' + data.result + '</p></div></li>');
			$(".panel-body").stop().animate({
				scrollTop: $(".panel-body")[0].scrollHeight
			}, 2000);
			$('input[name=query]').focus().select();
			state = 1;
		});
		return false;
	};

	$('a#sendbox').bind('click', function() {
		request();
		submit_form();
	});

	$('input[type=text]').bind('keydown', function(e) {
		if (e.keyCode == 13) {
			request();
			submit_form(e);
			e.preventDefault();
		}
	});

	$('input[name=query]').focus();
	var SpeechRecognition = SpeechRecognition || webkitSpeechRecognition;
	var SpeechRecognitionEvent = SpeechRecognitionEvent || webkitSpeechRecognitionEvent;

	function testSpeech() {
		$('#voiceBtn').disabled = true;
		$('#voice_icon').css({
			transition: 'color 1s ease',
			color:'#c21830',
		});

		var recognition = new SpeechRecognition();
		recognition.lang = 'zh-Hant-TW';
		recognition.interimResults = false;
		recognition.maxAlternatives = 1;

		recognition.start();

		recognition.onresult = function(event) {
			// The SpeechRecognitionEvent results property returns a SpeechRecognitionResultList object
			// The SpeechRecognitionResultList object contains SpeechRecognitionResult objects.
			// It has a getter so it can be accessed like an array
			// The first [0] returns the SpeechRecognitionResult at position 0.
			// Each SpeechRecognitionResult object contains SpeechRecognitionAlternative objects that contain individual results.
			// These also have getters so they can be accessed like arrays.
			// The second [0] returns the SpeechRecognitionAlternative at position 0.
			// We then return the transcript property of the SpeechRecognitionAlternative object
			var speechResult = event.results[0][0].transcript;
			$('#input_text').val(speechResult);
			request();
			submit_form();
			console.log('Confidence: ' + event.results[0][0].confidence);
		}

		recognition.onspeechend = function() {
			recognition.stop();
			$('#voice_icon').css('color', 'white', '!important');
			$('#voiceBtn').disabled = false;
		}

		recognition.onerror = function(event) {
			$('#voiceBtn').disabled = false;
			$('#voiceBtn').textContent = 'Start new test';
			$('#input_text').val('Error occurred in recognition: ' + event.error);
		}

	}

	$('#voiceBtn').click(function() {
		testSpeech()
	});
});
