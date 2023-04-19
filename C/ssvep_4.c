#include <stdio.h>
#include <stdbool.h>
#include <SDL2/SDL.h>

const int WINDOW_WIDTH = 1920;
const int WINDOW_HEIGHT = 1080;

int main(int argc, char *argv[]) {
    
    if (argc != 5) {
        printf("Usage: %s <freq1> <freq2> <freq3> <freq4>\n", argv[0]);
        return 1;
    }

    int frequencies[4];

    for (int i = 0; i < 4; i++) {
        frequencies[i] = atoi(argv[i + 1]);
        if (frequencies[i] <= 0) {
            printf("Invalid frequency. Please provide positive integer values.\n");
            return 1;
        }
    }

    if (SDL_Init(SDL_INIT_VIDEO) < 0) {
        printf("SDL could not initialize! SDL_Error: %s\n", SDL_GetError());
        return 1;
    }

    SDL_Window *window = SDL_CreateWindow("Multi Flicker",
                                          SDL_WINDOWPOS_CENTERED,
                                          SDL_WINDOWPOS_CENTERED,
                                          WINDOW_WIDTH, WINDOW_HEIGHT,
                                          SDL_WINDOW_SHOWN);
    if (window == NULL) {
        printf("Window could not be created! SDL_Error: %s\n", SDL_GetError());
        SDL_Quit();
        return 1;
    }

    SDL_Renderer *renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
    if (renderer == NULL) {
        printf("Renderer could not be created! SDL_Error: %s\n", SDL_GetError());
        SDL_DestroyWindow(window);
        SDL_Quit();
        return 1;
    }


    Uint32 intervals[4];
    Uint32 next_flicker[4];
    bool white[4] = {false, false, false, false};

    for (int i = 0; i < 4; i++) {
        intervals[i] = (Uint32)(1000.0 / (2* frequencies[i]));
        next_flicker[i] = SDL_GetTicks() + intervals[i];
    }

    bool quit = false;
    SDL_Event event;

    while (!quit) {
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_QUIT || (event.type == SDL_KEYDOWN && event.key.keysym.sym == SDLK_ESCAPE)) {
                quit = true;
            }
        }

        for (int i = 0; i < 4; i++) {
            if (SDL_GetTicks() >= next_flicker[i]) {
                white[i] = !white[i];
                next_flicker[i] += intervals[i];
            }
        }

        SDL_SetRenderDrawColor(renderer, 128, 128, 128, 255);
        SDL_RenderClear(renderer);

        for (int i = 0; i < 4; i++) {
            SDL_Rect segment;
            segment.w = WINDOW_WIDTH / 2;
            segment.h = WINDOW_HEIGHT / 2;
            segment.x = (i % 2) * segment.w;
            segment.y = (i / 2) * segment.h;

            SDL_SetRenderDrawColor(renderer, white[i] ? 255 : 0, white[i] ? 255 : 0, white[i] ? 255 : 0, 255);
            SDL_RenderFillRect(renderer, &segment);
        }

        SDL_RenderPresent(renderer);
    }

    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();
    return 0;
}

