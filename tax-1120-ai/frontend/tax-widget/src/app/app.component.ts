import { Component } from '@angular/core';
import { TaxService } from 'src/services/tax.services';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {

  selectedFile!: File;

  result: any = null;
  preview: any[] = [];
  advice: any[] = [];
  breakdown: any = {};

  totalLowConfidence = 0;
  loading = false;

  constructor(private taxService: TaxService) { }

  onFileSelected(event: any) {
    this.selectedFile = event.target.files[0];
  }

  onUpload() {
    if (!this.selectedFile) {
      alert("Please select file");
      return;
    }

    this.loading = true;

    this.taxService.uploadTB(this.selectedFile).subscribe({
      next: (res: any) => {

        console.log("API RESPONSE:", res);

        this.result = res.result || {};
        this.preview = res.preview || [];
        this.advice = res.advice || [];
        this.breakdown = res.category_breakdown || {};

        this.processInsights();

        this.loading = false;
      },
      error: (err) => {
        console.error(err);
        alert("Upload failed");
        this.loading = false;
      }
    });
  }

  processInsights() {
    this.totalLowConfidence = this.preview.filter(
      x => x.confidence < 0.6
    ).length;
  }
}