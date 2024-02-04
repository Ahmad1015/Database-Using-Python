// GET request
fetch('http://localhost:1000', {
    method: 'GET',
}).then(response => {
    return response.text();
}).then(data => {
    console.log(data);
}).catch((error) => {
    console.error('Error:', error);
});


let data = "Can you just give me  SQL to create a table called Customers with ID , name , email as columns, After that give me SQL to add 2 different entries and then display everything in that Table.Just give me the sql lines, dont give me any character apart from it";
// POST request
fetch('http://localhost:1000', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({value: data})  
}).then(response => {
    return response.text();
}).then(data => {
    console.log(data);
}).catch((error) => {
    console.error('Error:', error);
});
