function main() {
	var panel = 1

	$('#next').click(function() {
		panel = (panel + 1) % 3
		if (panel == 1) {
			$('.panel-1').slideToggle();
			$('.panel-3').slideToggle();
			$('#1-t').toggleClass('active');
			$('#3-t').toggleClass('active');
		} else if (panel == 2) {
			$('.panel-2').slideToggle();
			$('.panel-1').slideToggle();
			$('#2-t').toggleClass('active');
			$('#1-t').toggleClass('active');
		} else {
			$('.panel-3').slideToggle();
			$('.panel-2').slideToggle();
			$('#3-t').toggleClass('active');
			$('#2-t').toggleClass('active');
		}
	});

	$('#prev').click(function() {
		panel = (panel - 1) % 3
		if (panel == 1) {
			$('.panel-1').slideToggle();
			$('.panel-2').slideToggle();
			$('#1-t').toggleClass('active');
			$('#2-t').toggleClass('active');
		} else if (panel == 2) {
			$('.panel-2').slideToggle();
			$('.panel-3').slideToggle();
			$('#2-t').toggleClass('active');
			$('#3-t').toggleClass('active');
		} else {
			$('.panel-3').slideToggle();
			$('.panel-1').slideToggle();
			$('#3-t').toggleClass('active');
			$('#1-t').toggleClass('active');
		}
	});


}

$(document).ready(main);