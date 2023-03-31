/*
 * filter.ts
 *    Filter functions for Accordion and Buddy Chats.
 */

type reqsEntry = {
    classKey: string;
    tagColor: string;
    task_Name: string;
    due: Date;
    task_Weight: number; 
    task_grade: number; 
    task_goal: string; 
};

/* getReqs
 *   Sorts requirements from all user's classes earliest to latest
 *   @params - entries: Array<reqsEntry>
 *=====================================*/
function getReqs(entries: reqsEntry[]): Array<reqsEntry> {
    entries.sort((a, b) => {
        const aDate = a.due.toISOString();
        const bDate = b.due.toISOString();
        
        if (aDate < bDate) 
            return -1;
        if (aDate > bDate)
            return 1;
        return 0;
    });

    let sortedEntries: reqsEntry[] = [];
    if (entries.length < 5){
        for (let i = 0; i < entries.length; i++)
            sortedEntries.push(entries[i]);
    }
    else{
        for (let i = 0; i < 5; i++)
            sortedEntries.push(entries[i]);
    }
    return sortedEntries;
}

/* getChats
 *   Generates Buddy chats comprised of study goal reminders, 
 *   impending deadlines, tips, and encouragements.
 *   @params - entries: Array<reqsEntry>
 *=====================================*/
function getChats(entries: reqsEntry[]): Array<Object> {
    // These chats are always present.
    const playButtonString: string = "Press on the Play ▶ button on a class to start studying!";
    const goodHoomanString: string = "Good hooman!";
    const studyMoreString: string = "Let's study some study more!"

    // Constant chats that aren't always present
    const noUpcomingAssignmentString: string = "You have no upcoming deadlines.";

    // Template chats
    const upcomingAssignmentString: string = "You have an upcoming deadline, \"";
    const dueDateString: string = "It is due on "
    const forClassString: string = "for your class: "
    const classGoalVowelString: string = "Don't forget! You're aiming for an "
    const classGoalConsonantString: string = "Don't forget! You're aiming for a "

    const monthNames = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ];

    let chats: string[] = [playButtonString];
    let sortedEntries: reqsEntry[] = getReqs(entries);
    if (sortedEntries.length == 0) {
        chats.push(noUpcomingAssignmentString);
    }
    else {
        for (let i = 0; i < sortedEntries.length; i++) {
            let classKey: string  = sortedEntries[i].classKey;
            let assignmentName: string = sortedEntries[i].task_Name;
            let classGoal: string = sortedEntries[i].task_goal;
            let dueDate: string = monthNames[sortedEntries[i].due.getMonth()].concat(' ', sortedEntries[i].due.getDate().toString());
            
            let assignmentChatString = upcomingAssignmentString.concat(assignmentName, '\" ', forClassString, classKey, '. ', dueDateString, dueDate, '!');
            let classGoalChatString: string;
            if(classGoal){
                if (classGoal.includes('a') || classGoal.includes('A') || classGoal.includes('e') || classGoal.includes('F') ||classGoal.includes('f') || classGoal.includes('F'))
                    classGoalChatString = classGoalVowelString.concat(classGoal, ' ', forClassString, classKey, '!');
                else
                    classGoalChatString = classGoalConsonantString.concat(classGoal, ' ', forClassString, classKey, '!');
                chats.push(classGoalChatString);
            }
            chats.push(assignmentChatString);
        }
    }
    chats.push(studyMoreString);
    chats.push(goodHoomanString);
    return chats;
}

export default{
    getReqs,
    getChats
}
export { reqsEntry };
