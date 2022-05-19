$(document).ready(function() {
      $('.show-chart').click(function(){
            $('#charts').slideToggle();
            // alert('Show chart')
      });

      // Add Assets link clicked
      $('.xyz').click(function(){
            $('.table').hide();
            $('.paragraph').hide();
            $('#reports').hide();
            $('.message').text('Add New Asset');
            $('.form-section').show();
            $('.new').show();
      })

      // Add new asset button click
      $('.new').click(function(){
            $('.add').slideToggle();
            // $('.new').hide();
      })

      // Location button clicked
      $('.loc-maps').click(function(){
            $('.table').hide();
            $('.paragraph').hide();
            $('#reports').hide();
            $('.map').show();
      })

});