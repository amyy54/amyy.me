const pages = {
    "Projects": {
        "speedruns": {
            description: "Personal speedrun website.",
            url: "speedruns",
            fullName: "Speedrun Database"
        },
        "analyzer": {
            description: "Speedrun.com Verification Analyzer statistics, used for gathering verification information.",
            url: "analyzer",
            fullName: "SRDC-Verification-Analyzer"
        },
        "randomizer": {
            description: "Super Mario Odyssey randomizer web application.",
            url: "randomizer",
            fullName: "SMO-Randomizer-Web"
        },
        "damageless": {
            description: "Super Mario Odyssey damageless Leaderboard.",
            url: "damageless",
            fullName: "SMO Damageless Leaderboard"
        },
        "ootr-tracker": {
            description: "Ocarina of Time Randomizer note taking application.",
            url: "ootr-tracker",
            fullName: "OoTR Tracker"
        },
        "splitmaker": {
            description: "Splits parser for LiveSplit that creates a more evenly distributed comparison.",
            url: "splitmaker",
            fullName: "Splitmaker"
        },
        "livesplit": {
            description: "Page detailing LiveSplit projects I've done.",
            url: "livesplit",
            fullName: "LiveSplit"
        },
        "notetree": {
            description: "Personal note taking application.",
            url: "notetree",
            fullName: "Note Tree"
        }
    },
    "Misc.": {
        "simple": {
            description: "Simple list of pages one can jump to. Useful for non-JS browsers.",
            url: "simple",
            fullName: "Simple"
        },
        "docs": {
            description: "Documentation Site",
            url: "https://docs.amyy.me",
            fullName: "Documentation"
        },
        "gitweb": {
            description: "Random Git repositories I have elected not to put on GitHub",
            url: "https://git.amyy.me",
            fullName: "GitWeb"
        }
    }
};

function get_page_obj(input) {
    for (const section in pages) {
        for (const page in pages[section]) {
            if (page === input)
                return pages[section][page];
        }
    }
    return null;
}

function openPage(page) {
    let obj = get_page_obj(page);
    if (obj)
        window.open(obj.url);
}

function printSocials() {
    return "<span class=\"font-bold\">Twitter</span> - <a class=\"text-[#4044ff] hover:underline\" href=\"https://twitter.com/mini54_\">@mini54_</a><br><span class=\"font-bold\">GitHub</span> - <a class=\"text-[#4044ff] hover:underline\" href=\"https://github.com/Minibeast\">Minibeast</a><br><span class=\"font-bold\">Twitch</span> - <a class=\"text-[#4044ff] hover:underline\" href=\"https://twitch.tv/mini54__\">mini54__</a><br><span class=\"font-bold\">YouTube</span> - <a class=\"text-[#4044ff] hover:underline\" href=\"https://youtube.com/@mini54_\">Mini</a><br><span class=\"font-bold\">Discord</span> - Mini#7200";
}

function printVersion() {
    return GIT_VERSION;
}

function printPages() {
    let output = "";
    for (const section in pages) {
        output += "<span class=\"underline font-bold\">" + section + "</span><br>";
        for (const page in pages[section]) {
            output += "<a class=\"text-[#4044ff] hover:underline\" href=\"" + pages[section][page].url + "\">" + pages[section][page].fullName + "</a> - " + pages[section][page].description + " <span class=\"font-bold\">[" + page + "]</span><br>";
        }
    }
    return output.trim();
}

function printLs() {
    return "index.html        [[;blue;]sonic4/]        [[;blue;]yeah/]        private_key.pem        [[;blue;]sm64wrongwarp/]";
}

function printCat(input) {
    if (input === "private_key.pem") {
        return "-----BEGIN RSA PRIVATE KEY-----\n\
MIICXAIBAAKBgQDMyfgDgbEKSdjfbcH47UuPZn18AHH7oo7M/rIxV7C453Fy7rcq\n\
P8ROTKFmhLPju6PJ7G4cAtHoDkMCON58/7GcDVxFzxWpRyjJoTrNz3eE42YO7roP\n\
Hd/1/b9u0IXsJgGOEti1/CDWzFJShBZd0hZP96IjdzB2pnKjoAfUO2nh6QIDAQAB\n\
AoGBAMT7tQuycVgDJo/r5HwLzPWX0TY4u2sftxpqF38s6TlCrrat9hO2mJ30Sf/x\n\
v5NbxzWQrW1WLRB4v23gw+oajXxkF9TAcqg1BMovnaqgF6f+8jMxgs/ujmm8y8Qu\n\
5PRi2dlIyh8syPYZpwSpKmAu4w1rBdZREWtoPJ2ihQwPTx0BAkEA64qnczfZujhq\n\
YNPZIUfhXe2WJsc6PbFBTDFKHCFnQcJEc130trCyTo9AwH/Sjt0n+JuGqmGWhwHn\n\
9lL5RtWuYQJBAN6ThMxEwxKNov24tNOaUPSGfmkmKRc9YpRqajvqQQy3zPXlPfje\n\
HZHHOVSn5LSa1W2Wx6fqSgngYMP3TomZkIkCQHvsBw1nZPXEmLM4whPwbXGtfkII\n\
r2ulxmT/ya3jJSBDxR+tXwJ/FFCgrcCZf34KfO0fZkpd7YQ6TIAcR2otIgECQBaA\n\
z7JfWWGs1EfWvuGN/pVaa7lx1EG3QRpEUA1St9TzWFOcI9HfkxnEDLXUa7ke1mlI\n\
D1OYyneJKf9mJ5id4BECQBwJ1mBHKxxHTz3LQ6IdKUPgVWceQAt2uk3s3lPtL0m6\n\
gk5nB5swpziisfirGRcrWi0CygE0I3ssc6Xk7b3q08s=\n\
-----END RSA PRIVATE KEY-----";
    } else if (input === "index.html") {
        window.open(location.href);
    } else if (input.startsWith("sonic4/")) {
        window.open("https://wamwoowam.github.io/sonic4");
    } else if (input.startsWith("yeah/")) {
        return ":3";
    } else if (input.startsWith("sm64wrongwarp/")) {
        window.open("https://youtu.be/YduutOI7uxY");
    }
    return null;
}

function printHelp() {
    return "[[u;;]help] - Returns this output.\n[[u;;]version] - Returns the Git version of this site.\n[[u;;]socials] - Returns a list of my socials.\n[[u;;]pages] - Returns a list of all the pages available for this site.\n[[u;;]open <page>] - Opens the specified web page.";
}

$(document).ready(function() {
    $('body').terminal({
        version: function() {
            this.echo(printVersion());
        },
        open: function(page) {
            openPage(page);
        },
        socials: function() {
            this.echo(printSocials(), {raw: true});
        },
        pages: function() {
            this.echo(printPages(), {raw: true});
        },
        help: function() {
            this.echo(printHelp());
        },
        ls: function() {
            this.echo(printLs());
        },
        cat: function(file) {
            let output = printCat(file);
            if (output)
                this.echo(output);
        },
        whoami: function() {
            this.echo("root");
        }
    }, {
        greetings: "Hi! I don't have a website yet. But I do have a terminal. Enjoy!\nType [[u;;]help] for help, [[u;;]socials] for socials.",
        prompt: "$ "
    });
});
