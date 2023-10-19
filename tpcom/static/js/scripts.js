/*!
* Start Bootstrap - Modern Business v5.0.7 (https://startbootstrap.com/template-overviews/modern-business)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-modern-business/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

            var prevScrollpos = window.scrollY;
            window.onscroll = function() {
                var currentScrollPos = window.scrollY;
                if (prevScrollpos > currentScrollPos) {
                    document.getElementById("scrollNavbar").style.top = "0";
                } else {
                    document.getElementById("scrollNavbar").style.top = "-50px"; // Możesz dostosować wartość, aby pasek nawigacji zniknął bardziej lub mniej
                }
                prevScrollpos = currentScrollPos;
            }
