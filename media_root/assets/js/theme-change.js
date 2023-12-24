const toggleSwitch = document.querySelector('.theme-switch input[type="checkbox"]');
const currentTheme = localStorage.getItem('theme');

if (currentTheme) {
    document.documentElement.setAttribute('data-theme', currentTheme);
        console.log('light')

    if (currentTheme === 'dark') {
        toggleSwitch.checked = true;
        console.log('ddark')

    }



}

function switchTheme(e) {
    if (e.target.checked) {
        document.documentElement.setAttribute('data-theme', 'dark');
        localStorage.setItem('theme', 'dark');
        console.log('ddark')
    }
    else {        document.documentElement.setAttribute('data-theme', 'light');
          localStorage.setItem('theme', 'light');
        console.log('light')

    }
}

toggleSwitch.addEventListener('change', switchTheme, false);