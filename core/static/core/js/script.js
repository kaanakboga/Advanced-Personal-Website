document.addEventListener("DOMContentLoaded", function () {
    // Typing Animation
    const phrases = [
        "Information Systems Engineer",
        "Developer",
        "Problem Solver",
        "Clean Code Advocate",
        "Agile Team Player",
        "Scalable Systems Builder"
    ];

    const el = document.getElementById("typed");
    if (el) {
        let currentPhraseIndex = 0;
        let currentCharIndex = 0;
        let isDeleting = false;

        function type() {
            const currentPhrase = phrases[currentPhraseIndex];

            if (isDeleting) {
                currentCharIndex--;
            } else {
                currentCharIndex++;
            }

            el.textContent = currentPhrase.substring(0, currentCharIndex);

            if (!isDeleting && currentCharIndex === currentPhrase.length) {
                setTimeout(() => {
                    isDeleting = true;
                    type();
                }, 1000);
                return;
            } else if (isDeleting && currentCharIndex === 0) {
                isDeleting = false;
                currentPhraseIndex = (currentPhraseIndex + 1) % phrases.length;
            }

            setTimeout(type, isDeleting ? 50 : 100);
        }

        type();
    }


    // Butonu seç
document.addEventListener("DOMContentLoaded", function () {
    const scrollTopBtn = document.getElementById("scrollTopBtn");

    // Scroll olduğunda buton göster/gizle
    window.addEventListener("scroll", function () {
        if (window.scrollY > 200) {
            scrollTopBtn.style.display = "block";
        } else {
            scrollTopBtn.style.display = "none";
        }
    });

    // Hem butonun kendisine hem içindeki ikona tıklama yetkisi veriyoruz
    scrollTopBtn.addEventListener("click", function () {
        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });
    });

    const icon = scrollTopBtn.querySelector('i');
    if (icon) {
        icon.addEventListener("click", function (e) {
            e.stopPropagation();  // Tıklama ikonda kaybolmasın
            window.scrollTo({
                top: 0,
                behavior: "smooth"
            });
        });
    }
});



});
