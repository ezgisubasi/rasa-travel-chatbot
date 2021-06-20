const SOCKETIO_URL = 'http://localhost:4000';
const CHAT_BASE_URL = 'http://localhost:5000';
const DOWNSAMPLING_WORKER = './downsampling_worker.js';
// const socket = io.connect(SOCKETIO_URL, {});

// const initSocket = function() {
//     socket.on('connect', () => {
//         console.log('socket connected');
//     });

//     socket.on('disconnect', () => {
//         console.log('socket disconnected');
//     });

//     socket.on('recognize', (results) => {
//         console.log('recognized:', results);
//         addBotMessage(results.text)
//     });
// }



const addBotMessage = function(message) {


    var template = `<div class="message-container"><div class="message bot-message">${message}</div></div>`
    var messageContainer = document.getElementById('chatcontainer');
    messageContainer.innerHTML = messageContainer.innerHTML + template;
    messageContainer.scrollTop = messageContainer.scrollHeight;

}

const addHumanMessage = function(message) {
    var template = `<div class="message-container"><div class="message human-message" style="margin-left:auto">${message}</div></div>`

    var messageContainer = document.getElementById('chatcontainer');
    messageContainer.innerHTML = messageContainer.innerHTML + template;
    messageContainer.scrollTop = messageContainer.scrollHeight;

}

const doTextRequest = function(message) {
    return axios.post(`${CHAT_BASE_URL}/chat`, {
        query: message
    });
}

const enterListener = function(e) {
    if (e.keyCode === 13) {
        // e.preventDefault();
        var inputData = document.getElementById("inputbox");
        if (inputData.value !== "") {
            addHumanMessage(inputData.value);
            doTextRequest(inputData.value)
            .then(function (res) {
                console.log(res);
                res.data.forEach(printFunction);
                function printFunction(value,index,array)
                {
                    addBotMessage(value.reply);
                };

            }).catch(function (err) {
                console.error('Something went wrong');
                console.error(err);
            });
        }
        inputData.value = "";
    }
}

let shouldStop = true;
let stopped = true;