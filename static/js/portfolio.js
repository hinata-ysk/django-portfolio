$(document).ready(function () {
  var my_posts = $('[rel=tooltip]');

  var size = $(window).width();
  for (i = 0; i < my_posts.length; i++) {
    the_post = $(my_posts[i]);

    if (the_post.hasClass('invert') && size >= 767) {
      the_post.tooltip({ placement: 'left' });
      the_post.css('cursor', 'pointer');
    } else {
      the_post.tooltip({ placement: 'rigth' });
      the_post.css('cursor', 'pointer');
    }
  }

});

$('#collapseReumeButton').click(function(){
  $(this).hide();
});

$('div[name=portfolio_modal_thumbnail]>img').click(function(){
  var target = parseInt($(this).attr('data-slide-to'));
  // $(this).parents('.modal-body').find('.carousel').carousel(target);
  $(this).parents('div[name=portfolio_modal_image]').find('div[name=carouselIndicators]').carousel(target);
});