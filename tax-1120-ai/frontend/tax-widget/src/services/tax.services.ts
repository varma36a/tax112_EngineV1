import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({ providedIn: 'root' })
export class TaxService {

    private apiUrl = 'http://127.0.0.1:8000/upload-tb';

    constructor(private http: HttpClient) { }

    uploadTB(file: File) {
        const formData = new FormData();
        formData.append('file', file);
        return this.http.post(this.apiUrl, formData);
    }
}