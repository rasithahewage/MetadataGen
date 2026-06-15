export async function retrieveSuggestion(data) {
    const url = "/fullsuggestion";

    return await fetch(url, {
        "method": "POST",
        "headers": {
            "Content-Type": "application/json"
        },
        "body": JSON.stringify(data)
    })
        .then(response => {
            if(!response.ok){
                throw new Error("Error while getting suggestion");
            }
            return response.json();
    })
        .catch(error => {
            console.error(error);
        });
}