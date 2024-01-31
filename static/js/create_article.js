$(function(){
   $('#article_previewer_btn').click(function(){
       var converter = new showdown.Converter();
       var article_html = converter.makeHtml($('#content').val());
       $('#article_previewer').html(article_html);
   });
});