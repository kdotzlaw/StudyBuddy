/*
 * stores.js
 *    Pinia stores: Application-level state management.
 *    Used to store and export important refs and setter or getter functions that
 *    can be globally imported by any Vue component, module, or test suite.
 */

import { defineStore } from "pinia";
import { ref } from "vue";

export const useStore = defineStore('store', () => {

    /* sessionTimer
     *   Active session Timer class that stores user, class, and time elapsed
     *   setter @params - newTimer: Timer
     *=====================================*/
    const sessionTimer = ref(null);
    function setTimer(newTimer){
        sessionTimer.value = newTimer;
    }

    /* pageName
     *   Current page(route) name
     *   setter @params - newName: String 
     *=====================================*/
    const pageName = ref("Dashboard");
    function setPageName(newName){
        pageName.value = newName;
        return pageName.value
    }

    /* userId
     *   Authenticated user ID
     *   setter @params - newId: String
     *=====================================*/
    const userId = ref(null);
    function loginUser(newId){
        userId.value = newId;
    }
    function logoutUser(){  // unsetter
        userId.value = null;
        studyClass.value = null;
    }

    /* studyTime
     *   Time elapsed studying for session in seconds
     *   setter @params - time: Number
     *=====================================*/
    const studyTime = ref(0);
    function setStudyTime(time){
        if(time)
          studyTime.value = time;
    }

    /* studyClass
     *   Class being studied for in current Timer session
     *   setter @params - newClass: String
     *=====================================*/
    const studyClass = ref(null);
    function setStudyClass(newClass){
        studyClass.value = newClass;
    }

    /* isModalOpen
     *   Reflects if a modal is currently overlayed(toggled) on the app layout
     *   'Modified getter' toggleModal executes boolean negation and returns switched state
     *   getter @returns - Boolean
     *=====================================*/
    const isModalOpen = ref(false);
    function toggleModal(){
        isModalOpen.value = !isModalOpen.value;
        return isModalOpen.value;
    }

    /*   Manages modal display 
     *     modalTitle: Passed as a title prop to the Modal component
     *     modalContent: ID of the component or set of elements to display with ModalManager
     *     modalRender: HTML string to render inside the modal slot; Appears underneath modalContent
     *   setter @params - title: String, content: String, renderString: String
     *=====================================*/
    const modalTitle = ref("Modal Title");
    const modalContent = ref(null);
    const modalRender = ref("");
    function setModal(title="Modal Title", content=null, renderString=""){
        modalTitle.value = title;
        modalContent.value = content;
        modalRender.value = renderString;
        toggleModal();
    }

    /* uiSkin
     *   ID reference for custom background or component aesthetic styles
     *   setter @params - skin: String
     *=====================================*/
    const uiSkin = ref("skin-default");
    function updateSkin(skin="skin-default"){
        uiSkin.value = skin;
    }

    /* buddyChoice
     *   ID of buddy character to display in dashboard
     *   setter @params - skin: String
     *=====================================*/
    const buddyChoice = ref("Corgi");
    function updateBuddy(buddy="Corgi"){
        buddyChoice.value = buddy;
    }

    /* taskName
     *   Name of selected requirement to edit
     *   setter @params - name: String
     *=====================================*/
    const taskName = ref(null);
    function setTaskName(name=null){
        taskName.value = name;
    }

    /* reqSignal
     *   Detect new change in course requirement cards
     *   setter @params - signal: Boolean
     *=====================================*/
    const reqSignal = ref(false);
    function updateReqSignal(signal=false){
        reqSignal.value = signal;
    }

    /* gradeSignal
     *   Detect new change in course letter grade
     *   setter @params - signal: Boolean
     *=====================================*/
    const gradeSignal = ref(false);
    function updateGradeSignal(signal=false){
        gradeSignal.value = signal;
    }

    // Export refs and getter/setter functions
    return {
        sessionTimer, setTimer,
        pageName, setPageName,
        userId, loginUser, logoutUser,
        studyTime, studyClass, setStudyTime, setStudyClass,
        isModalOpen, toggleModal,
        modalTitle, modalContent, modalRender, setModal,
        uiSkin, updateSkin, buddyChoice, updateBuddy,
        taskName, setTaskName,
        reqSignal, updateReqSignal, gradeSignal, updateGradeSignal
    }
})