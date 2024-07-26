let tg = window.Telegram.WebApp;

tg.expand();

tg.MainButton.textColor = '#FFFFFF';
tg.MainButton.color = '#2cab37';

let item = "";

// Attach event listeners to all buttons
for (let i = 1; i <= 6; i++) {
	let btn = document.getElementById(`btn${i}`);
	let img = document.getElementById(`img${i}`);
	if (btn) {
		btn.addEventListener("click", function() {
			if (tg.MainButton.isVisible) {
				tg.MainButton.hide();
			} else {
				tg.MainButton.setText(`Вы выбрали товар ${i}!`);
				item = `${i}`;
				tg.MainButton.show();
			}
		});
	}
	if (img) {
		img.addEventListener("click", function() {
			this.classList.toggle('vibrate');
		});
	}
}

document.addEventListener('DOMContentLoaded', function () {
	const images = document.querySelectorAll('.img');
	images.forEach(image => {
		image.addEventListener('click', function () {
			image.classList.remove('bounce'); // Reset animation
			void image.offsetWidth; // Trigger reflow
			image.classList.add('bounce');
		});
	});
});