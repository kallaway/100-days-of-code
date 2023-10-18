<div>
    {{-- A good traveler has no fixed plans and is not intent upon arriving. --}}
    <h1>{{ $title }}</h1>

    <h3>{{ $name }}</h3>

    <form wire:submit="save">
        <label for="title"></label>
        <input type="text" id="title" wire:model.live="title">
        <button type="submit">Save</button>
    </form>
</div>
