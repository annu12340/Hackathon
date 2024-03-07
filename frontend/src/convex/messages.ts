import { mutation, query } from "./_generated/server";
import { v } from "convex/values";

export const send = mutation({
    args: { message: v.string(), status: v.string() },
    handler: async (ctx, { message, status }) => {
        // Send a new message.
        await ctx.db.insert("messages", { message, status });
    },
});

export const get = query({
    args: {},
    handler: async (ctx) => {
        return await ctx.db.query("messages").collect();
    },
});