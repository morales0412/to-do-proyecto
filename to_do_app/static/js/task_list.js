document.addEventListener("DOMContentLoaded", () => {
    const animatedItems = document.querySelectorAll("[data-animate]");
    const createToggle = document.querySelector("[data-create-toggle]");
    const createPanel = document.querySelector("[data-create-panel]");
    const createClose = document.querySelector("[data-create-close]");

    const focusFirstField = () => {
        if (!createPanel) {
            return;
        }

        const firstField = createPanel.querySelector("input, textarea, select");

        if (firstField) {
            firstField.focus();
        }
    };

    const openCreatePanel = () => {
        if (!createPanel || !createToggle) {
            return;
        }

        createPanel.hidden = false;
        createToggle.setAttribute("aria-expanded", "true");
        focusFirstField();
        createPanel.scrollIntoView({ behavior: "smooth", block: "start" });
    };

    const closeCreatePanel = () => {
        if (!createPanel || !createToggle) {
            return;
        }

        createPanel.hidden = true;
        createToggle.setAttribute("aria-expanded", "false");
        createToggle.focus();
    };

    if (createToggle && createPanel) {
        createToggle.addEventListener("click", () => {
            if (createPanel.hidden) {
                openCreatePanel();
            } else {
                closeCreatePanel();
            }
        });
    }

    if (createClose && createPanel) {
        createClose.addEventListener("click", closeCreatePanel);
    }

    document.addEventListener("keydown", (event) => {
        if (event.key === "Escape" && createPanel && !createPanel.hidden) {
            closeCreatePanel();
        }
    });

    if (!animatedItems.length) {
        return;
    }

    if (!("IntersectionObserver" in window)) {
        animatedItems.forEach((item) => item.classList.add("is-visible"));
        return;
    }

    const observer = new IntersectionObserver(
        (entries, currentObserver) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("is-visible");
                    currentObserver.unobserve(entry.target);
                }
            });
        },
        {
            threshold: 0.12,
        }
    );

    animatedItems.forEach((item) => observer.observe(item));
});
