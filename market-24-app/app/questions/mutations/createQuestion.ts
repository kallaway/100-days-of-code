import { resolver } from "blitz"
import db from "db"
import { z } from "zod"

export const CreateQuestion = z.object({
    text: z.string().nonempty({message: "You must enter a question."}),
    choices: z.array(z.object({text: z.string()})),
})

export default resolver.pipe(resolver.zod(CreateQuestion), resolver.authorize(), async (input) => {
  const question = await db.question.create({ 
      data: {
         ...input,
         choices: {create: input.choices},
      },
  })

  return question
})
