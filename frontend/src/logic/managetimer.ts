import Timer from "./timer";
import { useStore } from "../stores";
import { storeToRefs } from "pinia";

/* manageTimer
 *   Starts new Timer instance if no Timer running
 *   Pauses current Timer if provided class or user params are current
 *   Create new Timer instance if provided class or user params are new
 *   @params - userId: string , course: string
 */
function manageTimer(userId: String, course: String){
    const store = useStore();
    const { setTimer, setStudyTime } = store;
    const { sessionTimer, studyTime } = storeToRefs(store);
    if(!sessionTimer.value){
        initTimer(userId, course);
    }
    else{
        // No Timer when user not authenticated or logged out
        if(!userId){
            setTimer(null);
            setStudyTime(0);
            studyTime.value = 0;
        }
        // Start new Timer instance for new class
        else if(sessionTimer.value.getSessionUser() != userId || sessionTimer.value.getCurrentClass() != course){
            // commitTimer(userId, course, studyTime.value);
            initTimer(userId, course);
        }
        // Pause Timer for current class
        else{
            let timer = sessionTimer.value;
            if(timer.isPaused())
                timer.resume();
            else
                timer.pause();
        }
    }
}

// Initiate Timer class
function initTimer(userId: String, course: String){
    const store = useStore();
    const { setTimer } = store;
    setTimer(new Timer(userId, course));
}

/* commitTimer
 *   Writes total accumulated time to backend before Timer destroy
 *   Triggers: New timer init replacing old instance AND Logging out
 *   @params - userId: string , classId: string, total: number 
 */
function commitTimer(userId: String, classId: String, total: number){
    // Using hypothetical endpoint for now
    const host = 'http://localhost:5000';
    const apiUrl = '/api/' + classId + '/update_time_studied';
    fetch(host + apiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        mode: 'no-cors',
        body: total.toString()
    })
        .then(response => console.log(response))
        .then(data => {
            console.log('Success:', data);
        })
    .catch(error => {
        console.error('Error:', error);
    });
}

export default { manageTimer, initTimer, commitTimer }