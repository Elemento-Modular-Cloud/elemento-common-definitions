# Documentation for the VM Widgets json library

## Sections
The foreseen sections are:
* CPU
* RAM
* OS

## Widget properties

### `name` (mandatory)
Name of the widget as a string.

### `tooltip` (mandatory)
Short description of the widget function as a string.

### `long_desc`
Long description of the widget function as a string. If not present should be equal to the `tooltip`.

### `widget_type` (mandatory)
Widget type to be chosen among:
* `slider`: scale with ticks. Example config:
    ```json
    "config": {
        "min": 1,            // Minimum scale value. Mandatory

        "max": 256,          // Maximum scale value. Mandatory

        "default": 1,        // Initial scale value.
                             // Defaults to min

        "step_func": "log",  // Function used for ticks positions. Can be lin or log.
                             // Defaults to lin

        "step_size": 2,      // Step size (if step_func is lin) or log base (if step_func is log).
                             // Defaults to 1

        "unit": "GHz"        // String to append to the numerical value for rendering purposes.
                             // Defaults to empty string
    }
    ```

* `switch`: on/off switch. Example config:
    ```json
    "config": {
        "true_value": "Cores",      // String description for true value. Mandatory

        "false_value": "Threads",   // String description for false value. Mandatory

        "default": "true_value"     // Initial value (reference to one of the two values).
                                    // Defaults to true_value
    }
    ```

* `checkboxes`: multiple choice checkboxes. Example config:
    ```json
    "config": {
        "values": [                 // List of possible values. Mandatory
            "X86_32",
            "X86_64",
            "ARM_7",
            "ARM_8"
        ],

        "default": "X86_64"         // Initial value (reference to one of the possible values).
                                    // Defaults to no value selected
    }
    ```

* `dropdown_single`: single choice dropdown menu. Example config:
    ```json
    "config": {
        "values": [                 // List of possible values. Mandatory
            "3DNow!",
            "ABM",
            "ADX",
            "AES",
            "AMX",
            "AVX",
            "AVX2",
            "AVX-512",
            "BMI1"
        ]

        "default": "ABM"         // Initial value (reference to one of the possible values).
                                    // Defaults to no value selected
    }
    ```

* `dropdown_multi`: multiple choice dropdown menu. Example config:
    ```json
    "config": {
        "values": [                 // List of possible values. Mandatory
            "SME",
            "SMM",
            "SMX",
            "SSE",
            "SSE2",
            "SSE3",
            "SSE4.1",
            "SSE4.2",
            "SSE4a",
            "SSE5",
            "SSSE3"
        ],

        "default": "SSE2"           // Initial value (reference to one of the possible values).
                                    // Can be a list of references to possible values.
                                    // Defaults to no value selected
    }
    ```

* `radio`: mutually exclusive options. Example config:
    ```json
    "config": {
        "values": [                 // List of possible values. Mandatory
            "Linux",
            "Macos",
            "Windows"
        ],

        "default": "Linux"          // Initial value (reference to one of the possible values).
                                    // Defaults to no value selected
    }
    ```

### `output_type`
Expected output type. Might require a cast.

### `output_target` (mandatory)
`json` key in the request specification file the widget output value should be mapped to.