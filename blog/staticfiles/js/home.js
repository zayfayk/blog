document.addEventListener('DOMContentLoaded', function() {
    const postLinks = document.querySelectorAll('.post a');
    
    postLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            alert('You are about to read this post!');
        });
    });
});
