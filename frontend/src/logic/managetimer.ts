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
        // Destroy Timer when user not authenticated or logged out
        if(!userId){
            setTimer(null);
            setStudyTime(0);
            studyTime.value = 0;
        }
        // Start new Timer instance for new class
        else if(sessionTimer.value.getSessionUser() != userId || sessionTimer.value.getCurrentClass() != course){
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

export default { manageTimer }