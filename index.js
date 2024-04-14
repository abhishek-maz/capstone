function performAction() {
    // Get the input values from the user
    var instanceId = document.getElementById('instanceId').value;
    var instanceName = document.getElementById('instanceName').value;
    var amiId = document.getElementById('amiId').value;
    var action = document.getElementById('action').value;
    
    // Make an HTTP POST request to the backend Lambda function
    fetch('https://3df91pc5a4.execute-api.us-east-1.amazonaws.com/default/ec2-backend', {
        method: 'POST',
        body: JSON.stringify({ "instanceId": instanceId, "instanceName": instanceName, "amiId": amiId, "action": action })
    })
    .then(response => response.text())
    .then(data => {
        // Display the response from the Lambda function in the UI
        console.log(data);
        document.getElementById("instanceInfo").innerText = data;
    })
    .catch(error => console.error('Error:', error));
}

function listInstances() {
    // Make an HTTP POST request to the backend Lambda function to list instances
    fetch('https://3df91pc5a4.execute-api.us-east-1.amazonaws.com/default/ec2-backend', {
        method: 'POST',
        body: JSON.stringify({ "action": "list" })
    })
    .then(response => response.text())
    .then(data => {
        // Display the response from the Lambda function in the UI
        console.log(data);
        document.getElementById("instanceInfo").innerText = data;
    })
    .catch(error => console.error('Error:', error));
}

function uploadFile() {
    var fileInput = document.getElementById('fileUpload');
    var file = fileInput.files[0];

    if (!file) {
        alert('Please select a file.');
        return;
    }

    var formData = new FormData();
    formData.append('file', file);

    fetch('https://p18962gd62.execute-api.us-east-1.amazonaws.com/default/s3-backend', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (response.ok) {
            document.getElementById('uploadStatus').innerText = 'File uploaded successfully to S3.';
        } else {
            document.getElementById('uploadStatus').innerText = 'Error uploading file to S3.';
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('uploadStatus').innerText = 'Error uploading file to S3.';
    });
}
