// Login functionality
function handleLogin() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const errorMessage = document.getElementById('error-message');

    if (username === 'admin' && password === 'admin') {
        // Hide login page and show main content
        document.getElementById('login-page').style.display = 'none';
        document.getElementById('main-content').style.display = 'block';
    } else {
        // Show error message
        errorMessage.textContent = 'Invalid username or password. Please try again.';
    }
}

// Event listener for login button
document.getElementById('login-btn').addEventListener('click', handleLogin);

// Existing JavaScript logic
async function loadData(file) {
    const response = await fetch(file);
    return await response.json();
}

function displayLearningPath(student, mentors) {
    const recommendationsDiv = document.getElementById('recommendations');
    recommendationsDiv.innerHTML = `
        <p><strong>Workshops:</strong> ${student.interests.join(", ")}</p>
        <p><strong>Mentor:</strong> ${matchMentor(student, mentors).name}</p>
    `;
}

function matchMentor(student, mentors) {
    return mentors.find(mentor => mentor.expertise.some(e => student.interests.includes(e))) || mentors[0];
}

function generateQuiz(quizzes) {
    const quizContainer = document.getElementById('quiz-container');
    const randomQuiz = quizzes[Math.floor(Math.random() * quizzes.length)];
    quizContainer.innerHTML = `
        <p>${randomQuiz.question}</p>
        ${randomQuiz.options.map((opt, index) => `<button onclick="checkAnswer(${index}, ${randomQuiz.answer})">${opt}</button>`).join("")}
    `;
}

function checkAnswer(selected, correct) {
    alert(selected === correct ? "Correct Answer!" : "Wrong Answer. Try Again!");
}

function displayAttendance(attendanceData, studentId) {
    const attendanceDiv = document.getElementById('attendance-report');
    const studentAttendance = attendanceData.filter(record => record.student_id === studentId);
    attendanceDiv.innerHTML = `
        <p><strong>Total Workshops Attended:</strong> ${studentAttendance.length}</p>
        <ul>
            ${studentAttendance.map(record => `<li>${record.workshop_id} on ${record.date}</li>`).join("")}
        </ul>
    `;
}

async function init() {
    const students = await loadData('data/students.json');
    const mentors = await loadData('data/mentors.json');
    const quizzes = await loadData('data/quizzes.json');
    const attendanceData = await loadData('data/attendance.json');

    const student = students[0];
    displayLearningPath(student, mentors);
    generateQuiz(quizzes);
    displayAttendance(attendanceData, student.id);
}

document.addEventListener('DOMContentLoaded', init);
