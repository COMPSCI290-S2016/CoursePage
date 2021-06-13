                var data = new complex_array.ComplexArray(samples.length);
                data.map(function(value, i, n) {
                    value.real = samples[i];
                });
