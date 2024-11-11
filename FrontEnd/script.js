const API_URL = 'http://127.0.0.1:5000/register'; 

document.addEventListener("DOMContentLoaded", () => {
    fetchRegistrations();   

    const form = document.getElementById("registration-form");
    form.addEventListener("submit", handleFormSubmit);
});

async function fetchRegistrations() {
    const response = await fetch(API_URL);
    const registrations = await response.json();
    const tbody = document.querySelector("#registration-list tbody");
    tbody.innerHTML = '';

    registrations.forEach(reg => {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${reg.Name}</td>
            <td>${reg.Email}</td>
            <td>${reg.DateOfBirth}</td>
            <td>${reg.PhoneNumber || ""}</td>
            <td>${reg.Address || ""}</td>
            <td>
                <button class="edit" onclick="editRegistration(${reg.ID})">Edit</button>
                <button class="delete" onclick="deleteRegistration(${reg.ID})">Delete</button>
            </td>
        `;
        tbody.appendChild(row);
    });
}

async function handleFormSubmit(event) {
    event.preventDefault();

    const id = document.getElementById("registration-id").value;
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const dob = document.getElementById("dob").value;
    const phone = document.getElementById("phone").value;
    const address = document.getElementById("address").value;

    const data = { name, email, date_of_birth: dob, phone_number: phone, address };

    if (id) {
        await fetch(`${API_URL}/${id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
    } else {
        await fetch(API_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
    }

    form.reset();
    fetchRegistrations();
}

async function editRegistration(id) {
    const response = await fetch(`${API_URL}/${id}`);
    const reg = await response.json();

    document.getElementById("registration-id").value = reg.ID;
    document.getElementById("name").value = reg.Name;
    document.getElementById("email").value = reg.Email;
    document.getElementById("dob").value = reg.DateOfBirth;
    document.getElementById("phone").value = reg.PhoneNumber;
    document.getElementById("address").value = reg.Address;
}

async function deleteRegistration(id) {
    const isConfirmed = confirm("Are you sure you want to delete this registration?");
    
    if (isConfirmed) {
        await fetch(`${API_URL}/${id}`, { method: 'DELETE' });
        fetchRegistrations();
    }
}
