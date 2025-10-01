/* Aurora's Security Dojo - Bionic Reading Enhancement */

class BionicReading {
    constructor() {
        this.isActive = false;
        this.init();
    }

    init() {
        // Create toggle button
        this.createToggleButton();
        
        // Check for saved preference
        const savedPreference = localStorage.getItem('bionic-reading');
        if (savedPreference === 'true') {
            this.toggle();
        }
    }

    createToggleButton() {
        const button = document.createElement('button');
        button.className = 'bionic-toggle';
        button.textContent = '🧠 Bionic Reading';
        button.onclick = () => this.toggle();
        
        document.body.appendChild(button);
        this.toggleButton = button;
    }

    toggle() {
        this.isActive = !this.isActive;
        
        if (this.isActive) {
            this.enableBionicReading();
            this.toggleButton.classList.add('active');
            this.toggleButton.textContent = '🧠 Bionic ON';
            localStorage.setItem('bionic-reading', 'true');
        } else {
            this.disableBionicReading();
            this.toggleButton.classList.remove('active');
            this.toggleButton.textContent = '🧠 Bionic Reading';
            localStorage.setItem('bionic-reading', 'false');
        }
    }

    enableBionicReading() {
        // Apply bionic reading to all text elements
        const textElements = document.querySelectorAll('p, li, div:not(.bionic-toggle), span:not(.bionic-toggle)');
        
        textElements.forEach(element => {
            if (!element.dataset.originalText) {
                element.dataset.originalText = element.innerHTML;
            }
            
            element.classList.add('bionic-reading');
            element.innerHTML = this.convertToBionic(element.dataset.originalText);
        });
    }

    disableBionicReading() {
        // Restore original text
        const textElements = document.querySelectorAll('.bionic-reading');
        
        textElements.forEach(element => {
            element.classList.remove('bionic-reading');
            if (element.dataset.originalText) {
                element.innerHTML = element.dataset.originalText;
            }
        });
    }

    convertToBionic(text) {
        // Convert text to bionic reading format
        return text.replace(/\b(\w{1,3})\w*/g, (match, firstPart) => {
            if (match.length <= 3) {
                return `<span>${match}</span>`;
            }
            return `<span>${firstPart}</span>${match.substring(firstPart.length)}`;
        });
    }
}

// Initialize Bionic Reading when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new BionicReading();
});

// Export for potential module usage
if (typeof module !== 'undefined' && module.exports) {
    module.exports = BionicReading;
}
