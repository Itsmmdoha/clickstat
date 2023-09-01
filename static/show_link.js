document.addEventListener('DOMContentLoaded', function () {
    const linkElement = document.getElementById('link');
    const link = linkElement.getAttribute('title');
    const copyButton = document.getElementById('copy-button');
    const copyStatus = document.getElementById('copy-status');

    const maxLength = 40;
    const truncatedLink = link.length > maxLength ? link.substring(0, maxLength) + '...' : link;

    linkElement.textContent = truncatedLink;

    copyButton.addEventListener('click', function () {
        const textarea = document.createElement('textarea');
        textarea.value = link;
        document.body.appendChild(textarea);
        textarea.select();
        document.execCommand('copy');
        document.body.removeChild(textarea);

        copyStatus.style.display = 'block';
        copyButton.disabled = true;

        setTimeout(function () {
            copyStatus.style.display = 'none';
            copyButton.disabled = false;
        }, 1500);
    });
});
