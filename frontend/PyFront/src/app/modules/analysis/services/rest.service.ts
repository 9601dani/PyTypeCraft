import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})

export class RestService {

  private readonly URL: string = 'http://35.229.69.249:8000/';
  constructor( private httpClient: HttpClient ) { }

  public post(body:any):Observable<any>{
    return this.httpClient.post(this.URL+"analisis", body);
  }

  public c3d_post(body: any): Observable<any>{
    return this.httpClient.post(this.URL+"/c3d",body)
  }
}
