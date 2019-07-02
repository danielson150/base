function call_url(url) {
    $.ajax({
      url: url,
      complete: function(xhr, statusText) {
        if(statusText === 'success'){
            location.reload()
            console.log(statusText )
        } else {
            alert(xhr.status)
        }
      }
    })
}


function search(url) {
    let key = $('#search-key').val();
    window.open(url + key, '_self');
}
