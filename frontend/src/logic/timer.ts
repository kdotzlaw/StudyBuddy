export default class Timer{

    private userId: String;
    private currentClass: String;
    private time: Number; // in seconds
    
    public constructor(userId: String, currentClass: String, startTime: Number){
        this.userId = userId;
        this.currentClass = currentClass;
        this.time = startTime;
    }

    public start(): void{
        setInterval(function() {
            console.log("tick");
        }, 1000);
    }

    private getSessionUser(): String{
        return this.userId;
    }

    private getCurrentClass(): String{
        return this.currentClass;
    }

    private getTime(): Number{
        return this.time;
    }


}