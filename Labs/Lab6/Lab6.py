import numpy as np
import math
from PIL import Image, ImageDraw

class COMPLEX:
    def __init__(self, x, y):
        self.real = x
        self.imag = y
    
    def magnitude(self):
        return math.sqrt(self.real * self.real + self.imag * self.imag)
    
    def phase(self):
        return math.atan2(self.imag, self.real)

class FFT:
    def __init__(self, input_data):
        if isinstance(input_data, np.ndarray):
            self.grey_image = input_data
            self.width, self.height = input_data.shape
        elif isinstance(input_data, Image.Image):
            self.obj = input_data
            self.width, self.height = input_data.size
            self.read_image()
        else:
            raise ValueError("Invalid input data")
        
        self.fourier = np.empty((self.width, self.height), dtype=COMPLEX)
        self.output = np.empty((self.width, self.height), dtype=COMPLEX)
        self.fft_shifted = None
        self.fft_normal = None
        self.fft_log = None
        self.fft_phase_log = None
        self.fourier_magnitude = None
        self.fourier_phase = None
        self.fft_normalized = None
        self.fft_phase_normalized = None
    
    def read_image(self):
        self.grey_image = np.empty((self.width, self.height), dtype=int)
        pixels = np.array(self.obj, dtype=np.uint8)
        for i in range(self.width):
            for j in range(self.height):
                self.grey_image[i, j] = int(np.mean(pixels[j, i]))

    def display_image(self, image_array=None):
        if image_array is None:
            image_array = self.grey_image
        image = Image.new("L", (self.width, self.height))
        pixels = np.array(image, dtype=np.uint8)
        for i in range(self.width):
            for j in range(self.height):
                pixels[j, i] = image_array[i, j]
        return image
    
    def forward_fft(self):
        for i in range(self.width):
            for j in range(self.height):
                self.fourier[i, j] = COMPLEX(float(self.grey_image[i, j]), 0)
        self.output = self.fft_2d(self.fourier, self.width, self.height, 1)
    
    def fft_shift(self):
        self.fft_shifted = np.empty((self.width, self.height), dtype=COMPLEX)
        for i in range(self.width // 2):
            for j in range(self.height // 2):
                self.fft_shifted[i + (self.width // 2), j + (self.height // 2)] = self.output[i, j]
                self.fft_shifted[i, j] = self.output[i + (self.width // 2), j + (self.height // 2)]
                self.fft_shifted[i + (self.width // 2), j] = self.output[i, j + (self.height // 2)]
                self.fft_shifted[i, j + (self.height // 2)] = self.output[i + (self.width // 2), j]
    
    def remove_fft_shift(self):
        self.fft_normal = np.empty((self.width, self.height), dtype=COMPLEX)
        for i in range(self.width // 2):
            for j in range(self.height // 2):
                self.fft_normal[i + (self.width // 2), j + (self.height // 2)] = self.fft_shifted[i, j]
                self.fft_normal[i, j] = self.fft_shifted[i + (self.width // 2), j + (self.height // 2)]
                self.fft_normal[i + (self.width // 2), j] = self.fft_shifted[i, j + (self.height // 2)]
                self.fft_normal[i, j + (self.height // 2)] = self.fft_shifted[i + (self.width // 2), j]

            {
                for (i = 0; i < nx; i++)
                {
                    output[i, j].real = 0.0;
                    output[i, j].imag = 0.0;
                }
                BitRev(real, imag, nx);
                FFT(dir, Math.Log((double)nx, 2), real, imag);
                for (i = 0; i < nx; i++)
                {
                    output[i, j].real = real[i];
                    output[i, j].imag = imag[i];
                }
            }
            real = new double[ny];
            imag = new double[ny];
            for (i = 0; i < nx; i++)
            {
                for (j = 0; j < ny; j++)
                {
                    real[j] = output[i, j].real;
                    imag[j] = output[i, j].imag;
                }
                BitRev(real, imag, ny);
                FFT(dir, Math.Log((double)ny, 2), real, imag);
                for (j = 0; j < ny; j++)
                {
                    output[i, j].real = real[j];
                    output[i, j].imag = imag[j];
                }
            }
            return output;

        private void BitRev(double[] real, double[] imag, int n)
        {
            int i, j, k;
            double temp;
            j = 0;
            for (i = 0; i < n - 1; i++)
            {
                if (i < j)
                {
                    temp = real[i];
                    real[i] = real[j];
                    real[j] = temp;
                    temp = imag[i];
                    imag[i] = imag[j];
                    imag[j] = temp;
                }
                k = n / 2;
                while (k <= j)
                {
                    j -= k;
                    k /= 2;
                }
                j += k;
            }
        }

        private void FFT(int dir, double m, double[] real, double[] imag)
        {
            int n, i, i1, j, k, i2, l, l1, l2;
            double c1, c2, tx, ty, t1, t2, u1, u2, z;

            n = 1;
            for (i = 0; i < m; i++)
                n *= 2;

            c1 = -1.0;
            c2 = 0.0;
            l2 = 1;

            for (l = 0; l < m; l++)
            {
                l1 = l2;
                l2 <<= 1;
                u1 = 1.0;
                u2 = 0.0;

                for (j = 0; j < l1; j++)
                {
                    for (i = j; i < n; i += l2)
                    {
                        i1 = i + l1;
                        t1 = u1 * real[i1] - u2 * imag[i1];
                        t2 = u1 * imag[i1] + u2 * real[i1];
                        real[i1] = real[i] - t1;
                        imag[i1] = imag[i] - t2;
                        real[i] += t1;
                        imag[i] += t2;
                    }

                    z = u1 * c1 - u2 * c2;
                    u2 = u1 * c2 + u2 * c1;
                    u= z;
                }
                c2 = Math.Sqrt((1.0 - c1) / 2.0);
                if (dir == 1)
                    c2 = -c2;
                c1 = Math.Sqrt((1.0 + c1) / 2.0);
            }

            if (dir == 1)
            {
                for (i = 0; i < n; i++)
                {
                    real[i] /= n;
                    imag[i] /= n;
                }
            }
        }
