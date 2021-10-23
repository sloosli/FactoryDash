import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Injectable} from "@angular/core";

@Injectable()
export class SchedulePlanService {
  constructor(private readonly http: HttpClient) {}

  public getSpeedCheck(): Observable<any> {
    return  this.http.get('http://192.168.50.50:5000/api/kpi_index_value/88');
  }
}
