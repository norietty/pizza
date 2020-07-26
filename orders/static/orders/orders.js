document.addEventListener('DOMContentLoaded', () => {
    //var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    // remebring channel 
    //if (!localStorage.getItem('channel')) {
    //    var channel = document.querySelector('#channels-list').value;
    //    localStorage.setItem('channel', channel);

    //}
    //else {
    //    document.querySelector('#channels-list').value = localStorage.getItem('channel');
    //    var channel = document.querySelector('#channels-list').value;
    //}

    extras = document.querySelectorAll('.check');
    Array.from(extras).forEach((element) => {
        element.addEventListener('click', function(){
            price = this.parentNode.parentNode.getElementsByTagName('p')[1].innerHTML;
            if (this.checked) {
                newPrice = parseFloat(price) + 0.50
                this.parentNode.parentNode.getElementsByTagName('p')[1].innerHTML = newPrice.toFixed(2)
            }
            else {
                newPrice = parseFloat(price) - 0.50
                this.parentNode.parentNode.getElementsByTagName('p')[1].innerHTML = newPrice.toFixed(2)
            }
        });
    });
    add_item = document.querySelectorAll('.add')
    Array.from(add_item).forEach( (element) => {
        element.addEventListener('click', function(){
            parent_div = this.parentNode.parentNode
            dish_name = parent_div.getElementsByTagName('p')[0]
            price = parent_div.getElementsByTagName('p')[1]
            extras = parent_div.getElementsByTagName('form')
        });
    };

    );


});