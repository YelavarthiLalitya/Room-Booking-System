document.getElementById('checkRoomsBtn').addEventListener('click', function() {
    const expectedAttendance = document.getElementById('expectedAttendance').value;
    const eventDate = document.getElementById('eventDate').value;
    const startTime = document.getElementById('startTime').value;
    const endTime = document.getElementById('endTime').value;

    fetch('/check_available_rooms', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
            expectedAttendance: expectedAttendance,
            eventDate: eventDate,
            startTime: startTime,
            endTime: endTime
        })
    })
    .then(response => response.json())
    .then(data => {
        const roomSelect = document.getElementById('roomSelect');
        roomSelect.innerHTML = '<option value="">Select a room</option>';  // Clear previous options

        data.available_rooms.forEach(room => {
            const option = document.createElement('option');
            option.value = room;
            option.textContent = room;
            roomSelect.appendChild(option);
        });

        document.getElementById('availableRoomsDiv').style.display = 'block';  // Show room selection
    })
    .catch(error => {
        console.error('Error:', error);
    });
});


