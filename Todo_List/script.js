(function() {
    let toDoListArray = [];
    const form = document.querySelector('.form');
    const input = document.querySelector('.form__input');
    const ul = document.querySelector('.toDoList');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const itemId = Date.now().toString();
        const toDoItem = input.value;
        addItemToDOM(itemId, toDoItem);
        addItemToArray(itemId, toDoItem);
        input.value = '';
    });

    ul.addEventListener('click', function(event) {
        if (event.target.tagName === 'LI') {
            const itemId = event.target.getAttribute('data-id');
            removeItemFromDOM(itemId);
            removeItemFromArray(itemId);
        }
    });

    function addItemToDOM(itemId, toDoItem) {
        const li = document.createElement('li');
        li.setAttribute('data-id', itemId);
        li.textContent = toDoItem;
        ul.appendChild(li);
    }

    function addItemToArray(itemId, toDoItem) {
        toDoListArray.push({ id: itemId, text: toDoItem });
    }

    function removeItemFromDOM(id) {
        const liToRemove = document.querySelector(`[data-id="${id}"]`);
        liToRemove.remove();
    }

    function removeItemFromArray(id) {
        toDoListArray = toDoListArray.filter(item => item.id !== id);
    }
})();
