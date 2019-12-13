;(function($) {
  'use strict'

  /* ========================================================================= */
  /*	Page Preloader
  /* ========================================================================= */

  // window.load = function () {
  // 	document.getElementById('preloader').style.display = 'none';
  // }

  $(window).on('load', function() {
    $('#preloader').fadeOut('slow', function() {
      $(this).remove()
    })
  })

  //Hero Slider
  $('.hero-slider').slick({
    autoplay: false,
    infinite: true,
    arrows: true,
    prevArrow: "<button type='button' class='prevArrow'></button>",
    nextArrow: "<button type='button' class='nextArrow'></button>",
    dots: false,
    pauseOnFocus: false,
    pauseOnHover: false,
    speed: 4000,
    rtl: true,
  })
  $('.hero-slider').slickAnimation()

  //timeline for each slide change
  var bgImageClassObjs = $('.home-page__background-image')
  var firstBackground = bgImageClassObjs.eq(0)
  var secondBackground = bgImageClassObjs.eq(1)
  var thirdBackground = bgImageClassObjs.eq(2)
  var fourthBackground = bgImageClassObjs.eq(3)

  var homePageContentItems = $('.home-page__content-item')
  var firstContentItem = homePageContentItems.eq(0)
  var secondContentItem = homePageContentItems.eq(1)
  var thirdContentItem = homePageContentItems.eq(2)
  var fourthContentItem = homePageContentItems.eq(3)

  var inactiveBackgroundProps = {
    className: '-=home-page__background-image--active',
  }
  var activeBackgroundProps = {
    className: '+=home-page__background-image--active',
  }

  var activeContent = {
    className: '+=home-page__content-item--active',
    zIndex: 40,
  }

  var inactiveContent = {
    className: '-=home-page__content-item--active',
    zIndex: 30,
  }

  var secondProjectAnimate = new TimelineMax()
  secondProjectAnimate
    .to('.project-nav__list-item-bg', 3, { xPercent: 100 })
    .to(firstBackground, 1.5, { opacity: 0 }, 0)
    .to(firstBackground, 0, inactiveBackgroundProps, 0)
    .to(firstContentItem, 1.5, inactiveContent, 0)
    .to(secondBackground, 3, { opacity: 1 }, 0)
    .to(secondContentItem, 1.5, activeContent, 1.5)
    .to(secondBackground, 0, activeBackgroundProps, 0)

  var thirdProjectAnimate = new TimelineMax()
    .to('.project-nav__list-item-bg', 3, { xPercent: 200 })
    .to(secondBackground, 1.5, { opacity: 0 }, 0)
    .to(secondBackground, 0, inactiveBackgroundProps, 0)
    .to(secondContentItem, 1.5, inactiveContent, 0)
    .to(thirdBackground, 3, { opacity: 1 }, 0)
    .to(thirdContentItem, 1.5, activeContent, 1.5)
    .to(thirdBackground, 0, activeBackgroundProps, 0)

  var fourthProjectAnimate = new TimelineMax()
    .to('.project-nav__list-item-bg', 3, { xPercent: 300 })
    .to(
      '.project-nav__list-item-bg',
      3,
      { scaleX: 2, transformOrigin: 'left' },
      0
    )
    .to(thirdBackground, 1.5, { opacity: 0 }, 0)
    .to(thirdContentItem, 1.5, inactiveContent, 0)
    .to(thirdBackground, 0, inactiveBackgroundProps, 0)
    .to(fourthBackground, 3, { opacity: 1 }, 0)
    .to(fourthContentItem, 1.5, activeContent, 1.5)
    .to(fourthBackground, 0, activeBackgroundProps, 0)

  //combined timeline for all slide changes
  var navAnimate = new TimelineMax({ repeat: -1, repeatDelay: 3, yoyo: true })
  navAnimate
    .add(secondProjectAnimate, '+=3')
    .add(thirdProjectAnimate, '+=3')
    .add(fourthProjectAnimate, '+=3')

  //click functionality for nav bar
  var projectNavListItem = $('.project-nav__list-item')
  var unclickableProps = {
    className: '+=not-clickable',
  }
  var clickableProps = {
    className: '-=not-clickable',
  }

  projectNavListItem.click(function() {
    function killInfiniteSlide() {
      if (navAnimate.isActive()) navAnimate.kill()
    }

    killInfiniteSlide()
    //find current active background
    var backgrounds = $('.home-page__background-image')
    var currentActive = $('.home-page__background-image--active')
    var contentItems = $('.home-page__content-item')
    var activeBackgroundIndex = backgrounds.index(currentActive)
    var clickedNavIndex = projectNavListItem.index($(this)) - 1 //account for overlay

    if (clickedNavIndex != activeBackgroundIndex) {
      var percentToShift = clickedNavIndex * 100
      var animateProps = { xPercent: percentToShift }

      if (clickedNavIndex == 3) {
        animateProps.scaleX = 2
        animateProps.transformOrigin = 'left'
      }
      if (activeBackgroundIndex == 3) {
        animateProps.scaleX = 1
        animateProps.transformOrigin = 'left'
      }

      //animate to project
      var backgroundToActivate = backgrounds.eq(clickedNavIndex)
      var backgroundToHide = backgrounds.eq(activeBackgroundIndex)
      var contentToActivate = contentItems.eq(clickedNavIndex)
      var contentToHide = contentItems.eq(activeBackgroundIndex)

      var animateTransition = new TimelineMax()
      animateTransition
        .to(projectNavListItem, 0, unclickableProps, 0)
        .to(backgroundToHide, 0, inactiveBackgroundProps, 0)
        .to(contentToHide, 1.5, inactiveContent, 0)
        .to(backgroundToActivate, 0, activeBackgroundProps, 0)
        .to(contentToActivate, 1.5, activeContent, 1.5)
        .to(backgroundToActivate, 1.5, { opacity: 1 }, 0)
        .to(backgroundToHide, 3, { opacity: 0 }, 0)
        .to('.project-nav__list-item-bg', 3, animateProps, 0)
        .to(projectNavListItem, 0, clickableProps)
    }
  })

  /* ========================================================================= */
  /*	Header Scroll Background Change
  /* ========================================================================= */

  $(window).scroll(function() {
    var scroll = $(window).scrollTop()
    //console.log(scroll);
    if (scroll > 200) {
      //console.log('a');
      $('.navigation').addClass('sticky-header')
    } else {
      //console.log('a');
      $('.navigation').removeClass('sticky-header')
    }
  })

  /* ========================================================================= */
  /*	Portfolio Filtering Hook
  /* =========================================================================  */

  // filter
  // setTimeout(function() {
  //   var containerEl = document.querySelector(".filtr-container");
  //   var filterizd;
  //   if (containerEl) {
  //     filterizd = $(".filtr-container").filterizr({});
  //   }
  // }, 500);

  /* ========================================================================= */
  /*	Testimonial Carousel
  /* =========================================================================  */

  //Init the slider
  $('.testimonial-slider').slick({
    infinite: true,
    arrows: false,
    autoplay: true,
    autoplaySpeed: 2000,
  })

  /* ========================================================================= */
  /*	Clients Slider Carousel
  /* =========================================================================  */

  //Init the slider
  $('.clients-logo-slider').slick({
    infinite: true,
    arrows: false,
    autoplay: true,
    autoplaySpeed: 2000,
    slidesToShow: 5,
    slidesToScroll: 1,
  })

  /* ========================================================================= */
  /*	Company Slider Carousel
  /* =========================================================================  */
  $('.company-gallery').slick({
    infinite: true,
    arrows: false,
    autoplay: true,
    autoplaySpeed: 2000,
    slidesToShow: 5,
    slidesToScroll: 1,
  })

  /* ========================================================================= */
  /*   Contact Form Validating
  /* ========================================================================= */

  $('#contact-form').validate({
    rules: {
      name: {
        required: true,
        minlength: 4,
      },
      email: {
        required: true,
        email: true,
      },
      subject: {
        required: false,
      },
      message: {
        required: true,
      },
    },
    messages: {
      user_name: {
        required: "Come on, you have a name don't you?",
        minlength: 'Your name must consist of at least 2 characters',
      },
      email: {
        required: 'Please put your email address',
      },
      message: {
        required: 'Put some messages here?',
        minlength: 'Your name must consist of at least 2 characters',
      },
    },
    submitHandler: function(form) {
      $(form).ajaxSubmit({
        type: 'POST',
        data: $(form).serialize(),
        url: 'sendmail.php',
        success: function() {
          $('#contact-form #success').fadeIn()
        },
        error: function() {
          $('#contact-form #error').fadeIn()
        },
      })
    },
  })

  /* ========================================================================= */
  /*	On scroll fade/bounce effect
  /* ========================================================================= */
  var scroll = new SmoothScroll('a[href*="#"]')

  // -----------------------------
  //  Count Up
  // -----------------------------
  function counter() {
    if ($('.counter').length !== 0) {
      var oTop = $('.counter').offset().top - window.innerHeight
    }
    if ($(window).scrollTop() > oTop) {
      $('.counter').each(function() {
        var $this = $(this),
          countTo = $this.attr('data-count')
        $({
          countNum: $this.text(),
        }).animate(
          {
            countNum: countTo,
          },
          {
            duration: 1000,
            easing: 'swing',
            step: function() {
              $this.text(Math.floor(this.countNum))
            },
            complete: function() {
              $this.text(this.countNum)
            },
          }
        )
      })
    }
  }
  // -----------------------------
  //  On Scroll
  // -----------------------------
  $(window).scroll(function() {
    counter()
  })

  // nav selection
  $('.nav-item--secondary').click(function() {
    var currentActive = $('.nav-item--secondary.active')
    currentActive.removeClass('active')
    $(this).addClass('active')
  })
})(jQuery)
