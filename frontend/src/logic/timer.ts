export default class Timer{

    private userId: String;
    private currentClass: String;
    private startTime: Number;
    
    public constructor(userId: String, currentClass: String){
        this.userId = userId;
        this.currentClass = currentClass;
        this.startTime = Date.now();
    }

    public getSessionUser(): String{
        return this.userId;
    }

    public getCurrentClass(): String{
        return this.currentClass;
    }

    public getTime(): Number{
        return Date.now() - this.startTime;
    }

}