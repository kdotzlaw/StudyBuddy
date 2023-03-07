/*
 * managetimer.ts
 *    Global session timer management functions. Accesses the Timer instance 
 *    in stores.js that runs independently from component lifecycles.
 */

import Timer from "./timer";
import { useStore } from "../stores";
import { storeToRefs } from "pinia";

/* manageTimer
 *   Starts new Timer instance if no Timer running
 *   Pauses current Timer if provided class or user params are current
 *   Create new Timer instance if provided class or user params are new
 *   @params - userId: string , classId: string
 *=====================================*/
function manageTimer(userId: String, classId: String){
    const store = useStore();
    const { setTimer, setStudyTime } = store;
    const { sessionTimer, studyTime } = storeToRefs(store);
    if(!sessionTimer.value){
        initTimer(userId, classId);
    }
    else{
        // No Timer when user not authenticated or logged out
        if(!userId){
            setTimer(null);
            setStudyTime(0);
            studyTime.value = 0;
        }
        // Start new Timer instance for new class
        else if(sessionTimer.value.getSessionUser() != userId || sessionTimer.value.getCurrentClass() != classId){
            commitTimer(userId, classId, studyTime.value);
            initTimer(userId, classId);
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

/* initTimer
 *   Initialize new Timer class
 *   @params - userId: string , classId: string
 *=====================================*/
function initTimer(userId: String, classId: String){
    const store = useStore();
    const { setTimer } = store;
    setTimer(new Timer(userId, classId));
}

/* commitTimer
 *   Writes total accumulated time to backend before Timer destroy
 *   Triggers: New timer init replacing old instance, Logging out
 *   @params - userId: string , classId: string, total: number 
 *=====================================*/
function commitTimer(userId: String, classId: String, total: number){
    const host = 'http://127.0.0.1:5000';
    const apiUrl = '/api/' + classId + '/update_time';
    fetch(host + apiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        mode: 'no-cors',
        credentials: 'include',
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