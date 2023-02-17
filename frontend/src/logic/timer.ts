/*
 * timer.ts
 *    Timer class definition to store user and class keys, and time spent studying, 
 *    and functions to pause and resume timer.
 */

export default class Timer{

    private userId: String;
    private currentClass: String;
    private startTime: number;
    private pauseTotal: number = 0;  // Total of all intervals of paused times to deduct from study time
    private pauseStart: number = 0;
    private paused: boolean = false;

    public constructor(userId: String, currentClass: String){
        this.userId = userId;
        this.currentClass = currentClass;
        this.startTime = Date.now();
    }

    // Getters
    public getSessionUser(): String{
        return this.userId;
    }
    public getCurrentClass(): String{
        return this.currentClass;
    }
    public getTime(): Number{
        if(this.paused)
            return this.pauseStart - this.pauseTotal - this.startTime;
        else
            return Date.now() - this.pauseTotal - this.startTime;
    }
    public isPaused(): boolean{
        return this.paused;
    }

    // Pause Management
    public pause(): void{
        this.pauseStart = Date.now();
        this.paused = true;
    }
    public resume(): void{
        this.paused = false;
        this.pauseTotal += Date.now() - this.pauseStart;
    }

}